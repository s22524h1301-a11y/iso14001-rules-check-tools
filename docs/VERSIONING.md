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
- `v0.2.0` is the first reporting expansion release, adding CSV output and improved clause catalog/ranking
- `v0.3.0` tightens high-false-positive matching and makes the text/CSV reports easier to scan
- `v0.4.0` expands the clause catalog across the core ISO 14001 chapters without changing the pipeline or report formats
- `v0.5.0` strengthens the weaker `7.x` and `8.2` clause keywords to improve real-world document matching
- Future releases will move forward as the ISO 14001 clause catalog and analysis flow grow
