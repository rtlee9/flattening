# Repository Guidelines

## Project Structure & Module Organization
- `flatten.py`: Click-based CLI that generates G-code for flattening CNC wood slabs; keep the CLI slim and push logic to helpers.
- `index.html`: Standalone static web page with client-side JavaScript G-code generation; no server required — just open in a browser.
- `flattening_web/`: Django project settings/urls/wsgi for the web UI.
- `slabs/`: Django app with forms/views and shared G-code generation logic in `slabs/utils.py`.
- `templates/slabs/form.html`: Django web form for non-technical users.
- `tests/`: Pytest suite; add new tests near related modules.
- `readme.md`: User-facing usage notes; keep CLI/Web instructions aligned with options.
- `requirements.txt`: Runtime/dev dependencies; prefer adding libs here instead of ad-hoc installs.
- `LICENSE.txt`: MIT license; keep headers intact.

## Build, Test, and Development Commands
- Install deps: `python -m pip install -r requirements.txt`
- Run CLI: `python flatten.py` (prompts for width/length; other flags via CLI options)
- Run web app: `python manage.py runserver` then open http://127.0.0.1:8000/
- Tests: `pytest`
- Lint/format (recommended): `python -m pip install black` then `black flatten.py slabs`
- Optional type check: `python -m pip install mypy` then `mypy flatten.py slabs`

## Coding Style & Naming Conventions
- Follow PEP 8; prefer Black defaults (88-char lines, double quotes acceptable) and keep templates tidy.
- Functions: lowercase with underscores; constants like `SAFE_DISTANCE` stay uppercase.
- CLI options should match existing dash-separated flag style and map to snake_case parameters.
- Keep user-facing text concise; prefer explicit option help strings.

## Testing Guidelines
- No existing test suite; add targeted unit tests when changing path planning math or CLI parsing.
- Name tests `test_<area>.py`; group geometry/step calculations separately from CLI IO.
- Use `pytest`; keep fixtures minimal and prefer deterministic numeric assertions.
- When altering toolpath logic, validate with at least one numeric example (e.g., width=24, stepover=1.2) and confirm generated coordinates stay within bounds.

## Commit & Pull Request Guidelines
- Commits: present tense, scoped titles (`Add validation for skip-direction`) and concise bodies describing rationale and edge cases.
- Pull Requests: summarize behavior change, note CLI flags added/modified, and include before/after G-code snippets when applicable.
- Link related issues; request review on math-heavy changes; mention any new dependencies or setup steps.

## Security & Configuration Tips
- The tool emits G-code; confirm coordinates and safe heights before running on hardware. Avoid hard-coding machine-specific offsets.
- Do not commit machine calibration files or generated G-code outputs; keep working files local or git-ignored.
