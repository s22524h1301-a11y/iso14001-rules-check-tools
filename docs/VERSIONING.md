# Versioning and Commit Rules

This project uses SemVer-style versioning while it is still in active development.

## Version rules

- `patch` for documentation fixes, small bug fixes, and small behavior tweaks
- `minor` for a new working feature or a meaningful catalog expansion
- `major` for a breaking change to the API, CLI, or output format

## Commit types

- `docs:` documentation updates
- `feat:` new functionality
- `fix:` bug fixes
- `refactor:` code restructuring without behavior change
- `test:` test changes
- `chore:` maintenance or build changes

## Release flow

1. Update the version in `pyproject.toml`
2. Update `README.md` if the visible status changed
3. Add a changelog entry
4. Commit the change
5. Tag the release when the version is ready

## Starting point

- The project starts at `v0.1.0`
- `v0.1.1` is the first OCR stability patch and stays within the ISO 14001-only scope
- Future releases will move forward as the ISO 14001 clause catalog and analysis flow grow
