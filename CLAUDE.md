# CLAUDE.md - commit-info-extractor

GitHub Action to extract and process information from commit messages using customizable patterns and commands.

## Project Structure

```
entrypoint.py                    # Thin wrapper (calls app.main.run)
app/
  __init__.py
  main.py                       # Orchestration entrypoint
  config.py                     # AppConfig dataclass (from_env, validate)
  git_client.py                 # Git operations (configure, fetch commits)
  extractor.py                  # Shell command extraction logic
  formatter.py                  # Output formatting (text/json/csv)
  output_writer.py              # GITHUB_ENV/GITHUB_OUTPUT writing
  logger.py                     # Logging utilities (header, debug, error)
tests/
  __init__.py
  conftest.py                   # pytest fixtures (clean_env, default_env)
  test_config.py                # AppConfig unit tests
  test_extractor.py             # Extraction logic tests
  test_formatter.py             # Formatter tests
  test_git_client.py            # Git client tests
  test_output_writer.py         # Output writer tests
  test_main.py                  # Integration tests (mocked)
  test_local.py                 # Local integration test (requires git repo)
backup/
  entrypoint.py                 # Original single-file entrypoint
Dockerfile                      # Single-stage (python:3.14-slim)
action.yml                      # GitHub Action definition (8 inputs, 2 outputs)
requirements-dev.txt            # pytest, pytest-cov
.coveragerc                     # Coverage config
```

## Build & Test

```bash
# Unit tests with coverage (use venv)
python -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest tests/ -v --cov=app --cov-report=term-missing

# Local integration test (requires git repo)
python tests/test_local.py

# Run directly with INPUT_* env vars
python entrypoint.py
```

## Key Inputs

- **Required**: `commit_limit`
- **Options**: `extract_command`, `pretty`, `key_variable`, `fail_on_empty`, `output_format` (text/json/csv)
- **Advanced**: `debug`, `timeout`

## Outputs

`key_variable`, `value_variable`

## Workflow Structure

| Workflow | Name | Trigger |
|----------|------|---------|
| `ci.yml` | `Continuous Integration` | push(main), PR, dispatch |
| `release.yml` | `Create release` | tag push `v*` |
| `changelog-generator.yml` | `Generate changelog` | after release, PR merge, dispatch |
| `use-action.yml` | `Smoke Test (Released Action)` | after release, dispatch |
| `linter.yml` | `Lint Codebase` | dispatch |

### Workflow Chain
```
tag push v* -> Create release
                ├-> Smoke Test (Released Action)
                └-> Generate changelog
```

### CI Structure
```
unit-test ──────────┐
build-and-push-docker ──> test-action ──> ci-result
```

## Testing Notes

- Modular `app/` package with dataclass config, pytest fixtures, 90%+ coverage
- Local tests in `tests/test_local.py` for manual integration testing
- CI tests use `uses: ./` (local action) with various scenarios
- Smoke tests in `use-action.yml` use `somaz94/commit-info-extractor@v1` (released)
- Uses `subprocess.run` with shell=True for extract commands

## Conventions

- **Commits**: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `ci:`, `chore:`)
- **Branches**: `main` (production)
- **Secrets**: `PAT_TOKEN` (cross-repo ops), `GITHUB_TOKEN` (changelog, releases)
- **Docker**: Single-stage build, python:3.14-slim base
- **Comments**: English only
- **Release**: `git switch` (not `git checkout`), git-cliff for RELEASE.md
- **paths-ignore**: `.github/workflows/**`, `**/*.md`, `backup/**`
- **Testing**: pytest with coverage, fixtures in conftest.py
- Do NOT commit directly - recommend commit messages only
