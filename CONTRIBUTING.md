# Contributing

Thank you for helping keep Own the Recon accurate and safe.

## Before proposing a tool

A useful addition should have a clear role that is not already covered, an
official HTTPS source, an identifiable license, and evidence of active or stable
maintenance. Prefer upstream release assets and versioned package-manager
installs. Do not add:

- `curl | sh` or similar remote execution pipelines;
- floating installs when a release or commit can be pinned;
- system-wide Python installation commands;
- examples with real targets, credentials, aggressive rates, or destructive
  options;
- automated reconnaissance in GitHub Actions;
- copied upstream documentation that will immediately become stale.

If a project is archived or quiet, document that status explicitly. A legacy
entry can still be valuable when its limitations are clear.

## Updating a pin

1. Read the official release notes and installation documentation.
2. Check the release tag or full commit SHA from the upstream repository.
3. Update `tool-manifest.json`, `scripts/install-go-tools.sh`, and any visible
   version in `README.md` together.
4. Confirm the module path and required Go/Python version.
5. Run the local checks below.

## Local validation

```bash
python scripts/validate.py
bash -n scripts/install-go-tools.sh
bash scripts/install-go-tools.sh --dry-run
```

The installer dry run must not download, compile, scan, or modify the machine.

## Pull requests

Keep each change focused. Include links to primary upstream documentation,
explain the maintenance and safety impact, and describe how the commands were
validated. Never include target data, scan output, API keys, cookies, provider
configuration, or other engagement evidence.
