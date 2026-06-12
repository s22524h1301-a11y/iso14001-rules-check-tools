# ISO 14001 Rules Check Tools v0.4.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the ISO 14001 clause catalog across the core management system chapters so the matcher can recognize more realistic wording for `4.x`, `5.x`, `6.x`, `9.x`, and `10.x` sections without changing the PDF/OCR pipeline or the existing report formats.

**Architecture:** Keep the current pipeline intact: PDF intake, selectable-text extraction with OCR fallback, section splitting, clause matching, and reporting. `v0.4.0` is a catalog-growth release, so the main work happens in the clause catalog and the regression tests that prove the new coverage behaves as expected. The matcher should remain deterministic and explainable, and the reporting layer should continue to use the same text, JSON, and CSV contracts.

**Tech Stack:** Python 3.12, `pypdf`, OCR adapter layer, standard library `csv` and `json`, and `pytest`.

---

## File Structure

- `src/iso14001_rules_check_tools/clause_catalog.py` - expand and refine clause keywords and descriptions for the core management system chapters.
- `src/iso14001_rules_check_tools/matcher.py` - keep deterministic ranking intact and adjust only if a narrow scoring tweak is needed to support the expanded catalog.
- `src/iso14001_rules_check_tools/reporter.py` - no schema change expected, but keep reporting tests close to the new coverage so the existing text, JSON, and CSV outputs stay stable.
- `tests/test_matcher.py` - add regression tests for the newly expanded `4.x`, `5.x`, `6.x`, `9.x`, and `10.x` coverage.
- `tests/test_section_reporting.py` - confirm text reporting still renders after the catalog changes.
- `tests/test_csv_reporting.py` - confirm CSV reporting still renders after the catalog changes.
- `tests/test_docs.py` - update version/scope assertions for `v0.4.0`.
- `README.md` - refresh the visible version and catalog coverage summary.
- `CHANGELOG.md` - add the `v0.4.0` entry.
- `docs/VERSIONING.md` - record the new catalog-expansion release intent.
- `pyproject.toml` - bump the package version.

---

### Task 1: Add `4.x` coverage tests for context, scope, and EMS language

**Files:**
- Modify: `tests/test_matcher.py`
- Modify: `src/iso14001_rules_check_tools/clause_catalog.py`

- [ ] **Step 1: Write the failing test**

```python
from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def test_scope_language_matches_clause_4_3():
    section = Section(
        section_id="4.3.1",
        heading="Scope of the EMS",
        body="The scope of the environmental management system considers boundaries and applicability.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "4.3"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py -v`
Expected: the new `4.x` coverage test should fail until `4.3` is narrowed enough to outrank `4.4`.

- [ ] **Step 3: Write minimal implementation**

Expand `4.1`, `4.2`, `4.3`, and `4.4` in `src/iso14001_rules_check_tools/clause_catalog.py` with higher-signal keywords such as `internal issues`, `external issues`, `interested parties`, `scope`, `boundaries`, `applicability`, and `process interaction`. Remove or narrow the broad `processes`/`process interaction` overlap if `4.4` still outranks `4.3` for scope text.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py -v`
Expected: the `4.x` tests pass and the new keywords do not break existing `5.2` or `7.5` behavior.

- [ ] **Step 5: Commit**

```bash
git add tests/test_matcher.py src/iso14001_rules_check_tools/clause_catalog.py
git commit -m "feat: expand 4.x clause coverage"
```

---

### Task 2: Add `5.x` coverage tests for leadership, policy, and responsibility language

**Files:**
- Modify: `tests/test_matcher.py`
- Modify: `src/iso14001_rules_check_tools/clause_catalog.py`

- [ ] **Step 1: Write the failing test**

```python
from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def test_policy_language_matches_clause_5_2():
    section = Section(
        section_id="5.2.1",
        heading="Environmental policy",
        body="The environmental policy is established, communicated, and available as documented information.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "5.2"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py -v`
Expected: the new `5.x` coverage test should fail until the policy wording is strong enough to stay on `5.2`.

- [ ] **Step 3: Write minimal implementation**

Expand `5.1`, `5.2`, and `5.3` in `src/iso14001_rules_check_tools/clause_catalog.py` with more realistic keywords such as `top management`, `leadership`, `commitment`, `communicated`, `assigned`, and `authorities`. Keep the policy clause broad enough for real document wording but narrow enough to avoid accidental leadership-only matches.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py -v`
Expected: the `5.x` tests pass and existing policy matching stays stable.

- [ ] **Step 5: Commit**

```bash
git add tests/test_matcher.py src/iso14001_rules_check_tools/clause_catalog.py
git commit -m "feat: expand 5.x clause coverage"
```

---

### Task 3: Add `6.x` coverage tests for planning, obligations, and objectives

**Files:**
- Modify: `tests/test_matcher.py`
- Modify: `src/iso14001_rules_check_tools/clause_catalog.py`

- [ ] **Step 1: Write the failing test**

```python
from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def test_objective_language_matches_clause_6_2():
    section = Section(
        section_id="6.2.1",
        heading="Environmental objectives",
        body="The organization establishes measurable environmental objectives and plans actions to achieve them.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "6.2"


def test_planning_action_language_matches_clause_6_1_4():
    section = Section(
        section_id="6.1.4.1",
        heading="Planning action",
        body="The organization plans actions to address significant environmental aspects and compliance obligations.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "6.1.4"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py -v`
Expected: the new `6.x` coverage tests should fail until planning action wording is expanded and `6.2` beats `6.2.1` for broad objective text.

- [ ] **Step 3: Write minimal implementation**

Expand `6.1`, `6.1.1`, `6.1.2`, `6.1.3`, `6.1.4`, `6.2`, `6.2.1`, and `6.2.2` in `src/iso14001_rules_check_tools/clause_catalog.py` with explicit planning, aspect, obligation, objective, and action terms. If the objective clause still favors `6.2.1`, add a small disambiguating keyword set to `6.2.2` rather than broadening `6.2` further.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py -v`
Expected: the `6.x` tests pass and the false-positive controls from `v0.3.0` still hold.

- [ ] **Step 5: Commit**

```bash
git add tests/test_matcher.py src/iso14001_rules_check_tools/clause_catalog.py
git commit -m "feat: expand 6.x clause coverage"
```

---

### Task 4: Add `9.x` coverage tests for monitoring, compliance evaluation, audit, and review

**Files:**
- Modify: `tests/test_matcher.py`
- Modify: `src/iso14001_rules_check_tools/clause_catalog.py`

- [ ] **Step 1: Write the failing test**

```python
from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def test_compliance_evaluation_language_matches_clause_9_1_2():
    section = Section(
        section_id="9.1.2.1",
        heading="Evaluation of compliance",
        body="The organization periodically assesses compliance with legal and other requirements.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "9.1.2"


def test_internal_audit_language_matches_clause_9_2():
    section = Section(
        section_id="9.2.1",
        heading="Internal audit",
        body="The organization conducts internal audits and reports the results to management.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "9.2"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py -v`
Expected: the new `9.x` tests should fail until audit wording is strengthened and compliance evaluation stays on `9.1.2`.

- [ ] **Step 3: Write minimal implementation**

Expand `9.1`, `9.1.1`, `9.1.2`, `9.2`, and `9.3` in `src/iso14001_rules_check_tools/clause_catalog.py` with explicit monitoring, compliance evaluation, internal audit, and review terms. Keep `9.3` broad enough for management review language but not so broad that generic review text steals the match from `9.1` or `9.2`.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py -v`
Expected: the `9.x` tests pass.

- [ ] **Step 5: Commit**

```bash
git add tests/test_matcher.py src/iso14001_rules_check_tools/clause_catalog.py
git commit -m "feat: expand 9.x clause coverage"
```

---

### Task 5: Add `10.x` coverage tests for nonconformity and continual improvement

**Files:**
- Modify: `tests/test_matcher.py`
- Modify: `src/iso14001_rules_check_tools/clause_catalog.py`

- [ ] **Step 1: Write the failing test**

```python
from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def test_nonconformity_language_matches_clause_10_2():
    section = Section(
        section_id="10.2.1",
        heading="Nonconformity and corrective action",
        body="The organization reacts to nonconformity and takes corrective action to eliminate the cause.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "10.2"


def test_general_improvement_language_matches_clause_10_1():
    section = Section(
        section_id="10.1.1",
        heading="General improvement",
        body="The organization identifies opportunities for improvement and acts on them.",
    )

    matches = match_section(section, default_clause_catalog())
    assert matches[0].clause_id == "10.1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py -v`
Expected: the new `10.x` tests should fail until general improvement and corrective action wording is expanded.

- [ ] **Step 3: Write minimal implementation**

Expand `10.1`, `10.2`, and `10.3` in `src/iso14001_rules_check_tools/clause_catalog.py` with explicit nonconformity, corrective action, and continual improvement terms. Keep `10.3` distinct from `10.1` by emphasizing continual improvement language instead of generic improvement wording.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py -v`
Expected: the `10.x` tests pass.

- [ ] **Step 5: Commit**

```bash
git add tests/test_matcher.py src/iso14001_rules_check_tools/clause_catalog.py
git commit -m "feat: expand 10.x clause coverage"
```

---

### Task 6: Verify reports and docs still line up with the expanded catalog

**Files:**
- Modify: `tests/test_section_reporting.py`
- Modify: `tests/test_csv_reporting.py`
- Modify: `tests/test_docs.py`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `docs/VERSIONING.md`
- Modify: `pyproject.toml`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path


def test_readme_mentions_v040_and_catalog_expansion():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "v0.4.0" in readme
    assert "catalog" in readme.lower()
    assert "coverage" in readme.lower()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_docs.py -v`
Expected: the docs test should fail until versioned docs are updated.

- [ ] **Step 3: Write minimal implementation**

Bump `pyproject.toml` to `0.4.0`, update the README version and catalog coverage summary, add a `v0.4.0` changelog entry, and update `docs/VERSIONING.md` to describe the catalog-expansion release.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_docs.py -v`
Expected: docs assertions pass after the versioned text is refreshed.

- [ ] **Step 5: Commit**

```bash
git add README.md CHANGELOG.md docs/VERSIONING.md pyproject.toml tests/test_docs.py tests/test_section_reporting.py tests/test_csv_reporting.py
git commit -m "docs: prepare v0.4.0 catalog expansion release"
```

---

### Task 7: Full verification and release prep

**Files:**
- Review: all modified files from Tasks 1-6

- [ ] **Step 1: Run the full suite**

Run: `pytest -q`
Expected: all tests pass.

- [ ] **Step 2: Review the output manually**

Run a sample CLI analysis on a small PDF and confirm:
- the text report still renders cleanly
- the JSON output still has the same structure
- the CSV output still contains one row per match

- [ ] **Step 3: Commit any final fixes**

```bash
git add .
git commit -m "chore: finish v0.4.0 catalog expansion"
```

- [ ] **Step 4: Push the branch and prepare release notes**

```bash
git push origin main
```

Expected: the branch is up to date on GitHub and ready for a `v0.4.0` release tag once you decide to cut it.
