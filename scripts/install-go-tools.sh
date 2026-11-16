#!/usr/bin/env bash
set -euo pipefail

# This helper is intentionally a dry run unless --install is supplied. It never
# elevates privileges and installs only the versions recorded in the manifest.

readonly SCRIPT_NAME="${0##*/}"
MODE="dry-run"
BIN_DIR=""
declare -a SELECTED_TOOLS=()

readonly -a TOOL_SPECS=(
  "subfinder|github.com/projectdiscovery/subfinder/v2/cmd/subfinder@v2.17.0"
  "amass|github.com/owasp-amass/amass/v5/cmd/amass@v5.1.3"
  "assetfinder|github.com/tomnomnom/assetfinder@4e95d8701aae8cff1c27af2626eb22ba110ad583"
  "gobuster|github.com/OJ/gobuster/v3@v3.8.2"
  "httprobe|github.com/tomnomnom/httprobe@7e8abdb4096ab224f21616478b699b4dfda9d409"
  "waybackurls|github.com/tomnomnom/waybackurls@v0.1.0"
)

usage() {
  cat <<EOF
Usage: ${SCRIPT_NAME} [--dry-run | --install] [--tool NAME ...] [--bin-dir DIR]
       ${SCRIPT_NAME} --list

Options:
  --dry-run       Print the pinned commands without executing them (default).
  --install       Download, compile, and install the selected Go tools.
  --tool NAME     Limit the plan to one tool; repeat to select more than one.
  --bin-dir DIR   User-writable GOBIN destination.
  --list          List available names and pinned module specifications.
  -h, --help      Show this help.

Review tool-manifest.json and upstream release notes before using --install.
EOF
}

list_tools() {
  local entry name spec
  for entry in "${TOOL_SPECS[@]}"; do
    IFS='|' read -r name spec <<<"${entry}"
    printf '%-14s %s\n' "${name}" "${spec}"
  done
}

is_selected() {
  local candidate="$1"
  local selected

  if ((${#SELECTED_TOOLS[@]} == 0)); then
    return 0
  fi

  for selected in "${SELECTED_TOOLS[@]}"; do
    if [[ "${candidate}" == "${selected}" ]]; then
      return 0
    fi
  done
  return 1
}

is_known_tool() {
  local candidate="$1"
  local entry name spec
  for entry in "${TOOL_SPECS[@]}"; do
    IFS='|' read -r name spec <<<"${entry}"
    if [[ "${candidate}" == "${name}" ]]; then
      return 0
    fi
  done
  return 1
}

while (($#)); do
  case "$1" in
    --dry-run)
      MODE="dry-run"
      shift
      ;;
    --install)
      MODE="install"
      shift
      ;;
    --tool)
      if (($# < 2)); then
        printf 'error: --tool requires a name\n' >&2
        exit 2
      fi
      SELECTED_TOOLS+=("$2")
      shift 2
      ;;
    --bin-dir)
      if (($# < 2)); then
        printf 'error: --bin-dir requires a path\n' >&2
        exit 2
      fi
      BIN_DIR="$2"
      shift 2
      ;;
    --list)
      list_tools
      exit 0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'error: unknown option: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

for selected in "${SELECTED_TOOLS[@]}"; do
  if ! is_known_tool "${selected}"; then
    printf 'error: unknown tool: %s\n' "${selected}" >&2
    printf 'available tools:\n' >&2
    list_tools >&2
    exit 2
  fi
done

if [[ "${MODE}" == "install" ]]; then
  if ! command -v go >/dev/null 2>&1; then
    printf 'error: Go is required; install a supported toolchain first\n' >&2
    exit 1
  fi

  if [[ -z "${BIN_DIR}" ]]; then
    BIN_DIR="$(go env GOPATH)/bin"
  fi

  if [[ -z "${BIN_DIR}" || "${BIN_DIR}" == "/" ]]; then
    printf 'error: refusing unsafe bin directory: %s\n' "${BIN_DIR:-<empty>}" >&2
    exit 1
  fi

  mkdir -p -- "${BIN_DIR}"
  if [[ ! -d "${BIN_DIR}" || ! -w "${BIN_DIR}" ]]; then
    printf 'error: bin directory is not user-writable: %s\n' "${BIN_DIR}" >&2
    exit 1
  fi
fi

installed=0
entry=""
name=""
spec=""
for entry in "${TOOL_SPECS[@]}"; do
  IFS='|' read -r name spec <<<"${entry}"
  if ! is_selected "${name}"; then
    continue
  fi

  if [[ "${MODE}" == "dry-run" ]]; then
    printf 'GOBIN=<your-bin-dir> go install %q\n' "${spec}"
  else
    printf 'Installing %s from %s\n' "${name}" "${spec}"
    GOBIN="${BIN_DIR}" go install "${spec}"
  fi
  installed=$((installed + 1))
done

if ((installed == 0)); then
  printf 'error: no tools selected\n' >&2
  exit 2
fi

if [[ "${MODE}" == "dry-run" ]]; then
  printf '\nDry run only: no files were changed. Add --install after review.\n'
else
  printf '\nInstalled %d tool(s) into %s\n' "${installed}" "${BIN_DIR}"
  printf 'Add that directory to PATH if it is not already present.\n'
fi
