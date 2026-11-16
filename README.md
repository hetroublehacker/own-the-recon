# Own the Recon

[![Validate documentation](https://github.com/hetroublehacker/own-the-recon/actions/workflows/validate.yml/badge.svg)](https://github.com/hetroublehacker/own-the-recon/actions/workflows/validate.yml)

A practical, reviewable guide to reconnaissance tooling for authorized security
testing. It modernizes the tool list from the original
[Recon Like You Own It](https://medium.com/cyberverse/recon-like-you-owns-it-190175c81c42)
article without turning the repository into an opaque one-line installer.

> **Authorization is mandatory.** Only collect data from assets you own or have
> explicit permission to test. Respect the written scope, rate limits, provider
> terms, privacy rules, and stop conditions. Some "passive" tools query third
> parties; active probing, crawling, port scanning, fuzzing, and brute-force DNS
> can contact the target directly.

The catalog and pins were last reviewed on **2026-11-16**. Upstream projects
change quickly, so review release notes before upgrading.

## Why this version is safer

- Versioned Go installs replace obsolete installation commands.
- The helper is a dry run by default and never invokes `sudo`.
- Python tools use isolated environments instead of system-wide installs.
- Archived and quiet projects are labelled instead of presented as current.
- Examples use reserved domains and conservative behavior.
- CI validates the manifest, documentation, and installer without running any
  reconnaissance against the internet.

## Quick start

### 1. Define the engagement first

Record the following before selecting tools:

- in-scope domains, IP ranges, repositories, and cloud accounts;
- prohibited techniques and out-of-scope hosts;
- maximum request/concurrency rates and permitted testing windows;
- data retention, evidence handling, and emergency contacts.

Never infer that a related hostname, ASN, repository, or cloud bucket is in
scope. Discovery is not authorization.

### 2. Install prerequisites from trusted sources

Use your operating system's package manager or the vendor's official release
page for:

- Git;
- a currently supported Go toolchain;
- Python 3 with `venv` or `pipx`;
- CA certificates, `curl`, and an archive utility.

Do not copy a fixed Go tarball URL from an old guide. Several tools require a
newer Go version than others; their upstream release notes are authoritative.

After installing Go, make its binary directory available to your shell:

```bash
export PATH="$(go env GOPATH)/bin:$PATH"
```

### 3. Review the pinned Go plan

The included helper prints commands by default. It does not download or install
anything unless `--install` is supplied.

```bash
bash scripts/install-go-tools.sh --list
bash scripts/install-go-tools.sh --dry-run

# Install one reviewed tool without sudo:
bash scripts/install-go-tools.sh --install --tool subfinder

# Install every pinned Go tool after reviewing the plan:
bash scripts/install-go-tools.sh --install
```

Use `--bin-dir PATH` to choose a user-writable destination. The default is
`$(go env GOPATH)/bin`. All exact sources and versions are recorded in
[`tool-manifest.json`](tool-manifest.json).

## Core toolkit

| Phase | Tool | Status | Recommended installation path |
| --- | --- | --- | --- |
| Passive discovery | [Subfinder](https://github.com/projectdiscovery/subfinder) | Maintained | Pinned helper or upstream release |
| Attack-surface mapping | [OWASP Amass](https://github.com/owasp-amass/amass) | Maintained | Pinned helper, official binary, or official container |
| Passive discovery | [Findomain](https://github.com/Findomain/Findomain) | Maintained | Upstream release asset or Homebrew |
| DNS discovery | [Knockpy](https://github.com/guelfoweb/knockpy) | Maintained | Isolated Python environment |
| Passive discovery | [Assetfinder](https://github.com/tomnomnom/assetfinder) | Stable/quiet | Commit-pinned helper |
| DNS permutations | [AltDNS](https://github.com/infosec-au/altdns) | Stable/quiet | Isolated Python environment |
| Path discovery | [dirsearch](https://github.com/maurosoria/dirsearch) | Maintained | Isolated Python environment or upstream release |
| Path/DNS/vhost discovery | [Gobuster](https://github.com/OJ/gobuster) | Maintained | Pinned helper or upstream release |
| HTTP reachability | [httprobe](https://github.com/tomnomnom/httprobe) | Stable/quiet | Pinned helper |
| Historical URLs | [waybackurls](https://github.com/tomnomnom/waybackurls) | Stable/quiet | Pinned helper |

### Isolated Python examples

Keep each tool outside the system Python. Inspect the selected tag and its
dependency files before installation.

```bash
# Knockpy 9.0.0
python3 -m venv "$HOME/.venvs/knockpy"
"$HOME/.venvs/knockpy/bin/python" -m pip install --upgrade pip
"$HOME/.venvs/knockpy/bin/pip" install "knock-subdomains==9.0.0"

# dirsearch 0.5.0 from its official tagged source
python3 -m venv "$HOME/.venvs/dirsearch"
"$HOME/.venvs/dirsearch/bin/python" -m pip install --upgrade pip
"$HOME/.venvs/dirsearch/bin/pip" install \
  "git+https://github.com/maurosoria/dirsearch.git@v0.5.0"

# AltDNS: mature but quiet; test it in an isolated environment
python3 -m venv "$HOME/.venvs/altdns"
"$HOME/.venvs/altdns/bin/python" -m pip install --upgrade pip
"$HOME/.venvs/altdns/bin/pip" install "py-altdns==1.0.2"
```

For Findomain, prefer the assets on the project's
[release page](https://github.com/Findomain/Findomain/releases) and verify any
published checksums before execution. Avoid piping remote scripts into a shell.

## A conservative workflow

The commands below demonstrate data flow with the IANA-reserved `example.com`.
Replace it only with a scope-approved domain. Start passive, deduplicate at each
boundary, and add active steps only when the rules of engagement allow them.

```bash
mkdir -p results

# Passive collection. Some providers require API credentials and have their own
# terms and quotas.
subfinder -d example.com -silent -o results/subfinder.txt
assetfinder --subs-only example.com > results/assetfinder.txt

# Normalize before another tool consumes the data.
cat results/subfinder.txt results/assetfinder.txt \
  | sed '/^[[:space:]]*$/d' \
  | sort -u > results/subdomains.txt
```

Before active validation or content discovery:

1. remove third-party/CDN/shared-service names that are outside scope;
2. confirm permitted ports, paths, methods, and authentication state;
3. set an explicit low request rate and concurrency;
4. save timestamps, tool versions, configuration, and operator identity;
5. stop on instability, unexpected data exposure, or scope ambiguity.

Do not feed unreviewed discovery output directly into port scanners, crawlers,
fuzzers, or vulnerability templates.

## Modern extensions

These projects cover common gaps in the original article. They are deliberately
not included in the bulk installer: read their current documentation, choose a
specific release, and add only what the engagement needs.

| Capability | Project | Important guardrail |
| --- | --- | --- |
| DNS resolution | [dnsx](https://github.com/projectdiscovery/dnsx) | Resolve only approved names and resolvers |
| HTTP metadata/screenshots | [httpx](https://github.com/projectdiscovery/httpx) | Treat probing and screenshots as active access |
| Port discovery | [naabu](https://github.com/projectdiscovery/naabu) | Use explicit scope and conservative rate limits |
| Crawling | [Katana](https://github.com/projectdiscovery/katana) | Limit depth, hosts, forms, and authenticated state |
| Template-based checks | [Nuclei](https://github.com/projectdiscovery/nuclei) | Review templates and exclude intrusive checks |
| Content discovery | [ffuf](https://github.com/ffuf/ffuf) | Cap concurrency/rate and avoid state-changing methods |
| Historical URLs | [gau](https://github.com/lc/gau) | Validate provider terms and filter third parties |
| Screenshots | [gowitness](https://github.com/sensepost/gowitness) | Screens may capture personal or sensitive data |

## Legacy references

These tools appeared in the original guide but should not be the default choice
for a new environment:

| Tool | Reason |
| --- | --- |
| [Aquatone](https://github.com/michenriksen/aquatone) | Upstream repository is archived; keep only for reproducible legacy workflows |
| [WebScreenshot](https://github.com/maaaaz/webscreenshot) | Quiet project with an older dependency model; isolate and review before use |
| [LazyS3](https://github.com/nahamsec/lazys3) | Historical proof-of-concept; cloud enumeration can cross scope boundaries |

No legacy tool is installed by the helper.

## Credentials and evidence

- Put API keys in the tool's documented user configuration or an approved
  secret manager, not commands, shell history, screenshots, or this repository.
- Use separate low-privilege keys for research and rotate them after exposure.
- Do not commit provider configuration, `.env` files, raw results, session
  databases, cookies, authorization headers, or screenshots.
- Encrypt sensitive evidence and follow the program's retention policy.

The repository's `.gitignore` covers common local result and secret files, but
it is not a substitute for reviewing `git diff --staged` before every commit.

## Maintenance

Validate a change locally before opening a pull request:

```bash
python scripts/validate.py
bash -n scripts/install-go-tools.sh
bash scripts/install-go-tools.sh --dry-run
```

The workflow performs only static validation. It intentionally never installs
the tools or scans a target. See [CONTRIBUTING.md](CONTRIBUTING.md) for update
requirements and [SECURITY.md](SECURITY.md) for sensitive reports.

## Credits

All tools belong to their respective maintainers and contributors. This
repository provides a curated index and safety-focused installation guidance;
it does not redistribute their code or imply endorsement. Follow each project's
license and acceptable-use terms.
