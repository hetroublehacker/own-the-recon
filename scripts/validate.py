#!/usr/bin/env python3
"""Validate the curated manifest and its user-facing documentation."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "tool-manifest.json"
README_PATH = ROOT / "README.md"
INSTALLER_PATH = ROOT / "scripts" / "install-go-tools.sh"

ALLOWED_STATUSES = {"maintained", "stable"}
PIN_PATTERN = re.compile(r"^(?:v?\d+(?:\.\d+){1,3}|[0-9a-f]{40})$")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def load_json(path: Path, check: Validation) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        check.errors.append(f"cannot load {path.relative_to(ROOT)}: {exc}")
        return {}


def valid_github_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return (
        parsed.scheme == "https"
        and parsed.netloc.lower() == "github.com"
        and len([part for part in parsed.path.split("/") if part]) >= 2
        and not parsed.query
        and not parsed.fragment
    )


def validate() -> list[str]:
    check = Validation()
    manifest = load_json(MANIFEST_PATH, check)
    if not manifest:
        return check.errors

    check.require(manifest.get("schema_version") == 1, "schema_version must be 1")

    reviewed = manifest.get("reviewed")
    try:
        reviewed_date = date.fromisoformat(reviewed)
        check.require(reviewed_date <= date.today(), "reviewed date cannot be in the future")
    except (TypeError, ValueError):
        check.errors.append("reviewed must use YYYY-MM-DD")

    readme = README_PATH.read_text(encoding="utf-8")
    installer = INSTALLER_PATH.read_text(encoding="utf-8")
    check.require(str(reviewed) in readme, "README must show the manifest review date")
    check.require(readme.count("```") % 2 == 0, "README has an unclosed code fence")

    relative_links = re.findall(r"\]\((?!https?://|#)([^)]+)\)", readme)
    for link in relative_links:
        path_part = link.split("#", 1)[0]
        check.require(
            bool(path_part) and (ROOT / path_part).is_file(),
            f"README relative link does not resolve: {link}",
        )

    all_names: set[str] = set()
    all_sources: set[str] = set()
    sections = ("go_tools", "other_tools", "extensions", "legacy_tools")
    for section in sections:
        entries = manifest.get(section)
        check.require(isinstance(entries, list) and bool(entries), f"{section} must be a non-empty list")
        if not isinstance(entries, list):
            continue

        for index, entry in enumerate(entries):
            label = f"{section}[{index}]"
            check.require(isinstance(entry, dict), f"{label} must be an object")
            if not isinstance(entry, dict):
                continue

            name = entry.get("name")
            source = entry.get("source")
            check.require(
                isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9-]+", name)),
                f"{label}.name must be lowercase kebab-case",
            )
            if isinstance(name, str):
                check.require(name not in all_names, f"duplicate tool name: {name}")
                all_names.add(name)

            check.require(valid_github_url(source), f"{label}.source must be a clean GitHub HTTPS URL")
            if isinstance(source, str):
                check.require(source not in all_sources, f"duplicate source URL: {source}")
                all_sources.add(source)
                check.require(source in readme, f"README does not reference {source}")

    go_tools = manifest.get("go_tools", [])
    manifest_specs: set[str] = set()
    for entry in go_tools if isinstance(go_tools, list) else []:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name", "<unknown>")
        module = entry.get("module")
        version = entry.get("version")
        status = entry.get("status")
        check.require(
            isinstance(module, str) and module.startswith("github.com/") and " " not in module,
            f"{name}: invalid Go module",
        )
        check.require(
            isinstance(version, str) and bool(PIN_PATTERN.fullmatch(version)),
            f"{name}: version must be a semantic release or full commit SHA",
        )
        check.require(status in ALLOWED_STATUSES, f"{name}: unsupported status {status!r}")
        if isinstance(module, str) and isinstance(version, str):
            spec = f"{module}@{version}"
            manifest_specs.add(spec)
            check.require(spec in installer, f"installer is missing pinned spec {spec}")

    installer_specs = set(
        re.findall(r'"[a-z0-9-]+\|(github\.com/[^"|\s]+@[^"|\s]+)"', installer)
    )
    check.require(
        installer_specs == manifest_specs,
        "installer specs must exactly match the Go manifest",
    )

    other_tools = manifest.get("other_tools", [])
    for entry in other_tools if isinstance(other_tools, list) else []:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name", "<unknown>")
        check.require(entry.get("status") in ALLOWED_STATUSES, f"{name}: invalid status")
        version = entry.get("version")
        check.require(
            isinstance(version, str) and bool(PIN_PATTERN.fullmatch(version)),
            f"{name}: version must be pinned",
        )

    legacy_tools = manifest.get("legacy_tools", [])
    for entry in legacy_tools if isinstance(legacy_tools, list) else []:
        if isinstance(entry, dict):
            check.require(bool(entry.get("reason")), f"{entry.get('name')}: legacy reason is required")

    forbidden_snippets = {
        "go get ": "obsolete Go installation command",
        "@latest": "floating tool version",
        "sudo python setup.py": "unsafe system Python installation",
        "python-pip": "obsolete Python 2 package",
        "rm -rf": "destructive installation instruction",
        "--rate=10000": "aggressive scan-rate example",
    }
    combined = readme + "\n" + installer
    for snippet, explanation in forbidden_snippets.items():
        check.require(snippet not in combined, f"found {explanation}: {snippet!r}")

    remote_shell_pattern = re.compile(
        r"(?:curl|wget)[^\n|]*\|\s*(?:ba|z|k)?sh(?:\s|$)", re.IGNORECASE
    )
    check.require(
        not remote_shell_pattern.search(combined),
        "found an unreviewable remote shell pipeline",
    )

    check.require("--dry-run" in installer, "installer must support --dry-run")
    check.require("--install" in installer, "installer must require an explicit install mode")
    check.require('MODE="dry-run"' in installer, "installer must default to dry-run mode")
    check.require("sudo" not in installer, "installer must not elevate privileges")
    check.require("@latest" not in installer, "installer must not use floating Go versions")

    return check.errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Validated tool manifest, README references, and pinned installer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
