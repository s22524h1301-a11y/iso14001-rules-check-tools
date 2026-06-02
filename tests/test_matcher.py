from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def _pick_catalog(*clause_ids: str):
    catalog = default_clause_catalog()
    return tuple(clause for clause in catalog if clause.clause_id in clause_ids)


def test_environmental_policy_section_prefers_clause_5_2():
    section = Section(
        section_id="2.1",
        heading="Environmental policy",
        body="The organization shall establish an environmental policy and communicate it to employees.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.2"


def test_empty_catalog_returns_no_matches():
    section = Section(
        section_id="9.9",
        heading="Anything",
        body="No clause keywords here.",
    )

    matches = match_section(section, ())

    assert matches == ()


def test_heading_title_hit_ranks_above_body_only_hit():
    section = Section(
        section_id="2.1",
        heading="Communication",
        body="The organization reviews internal issues, external issues, the organization context, and environmental context.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.4"
    assert any(match.clause_id == "4.1" for match in matches)
    assert matches[0].score > next(match.score for match in matches if match.clause_id == "4.1")


def test_keyword_only_match_has_positive_score():
    section = Section(
        section_id="9.2.2",
        heading="Process review",
        body="The auditor reviewed the process and confirmed the findings.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "9.2"
    assert matches[0].score > 0
    assert "matched keywords" in matches[0].reason


def test_policing_words_do_not_create_false_matches():
    section = Section(
        section_id="4.2",
        heading="Process note",
        body="Our policymaking process and document records are kept internally.",
    )

    matches = match_section(section, default_clause_catalog())

    assert [match.clause_id for match in matches] == ["7.5"]


def test_non_matches_are_excluded():
    section = Section(
        section_id="x",
        heading="Unrelated note",
        body="This text does not reference any ISO 14001 clause keywords.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches == ()


def test_single_clear_keyword_match_is_kept_without_title_hit():
    section = Section(
        section_id="5.2.1",
        heading="Internal memo",
        body="policy",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.2"


def test_matcher_returns_all_positive_matches_without_truncation():
    section = Section(
        section_id="x",
        heading="Environmental policy documented information objective background context",
        body="organization environmental policy communicate environmental objectives planning documented information records context internal issues external issues",
    )
    catalog = _pick_catalog("4.1", "5.2", "6.2", "7.5")

    matches = match_section(section, catalog)

    assert {match.clause_id for match in matches} == {"4.1", "5.2", "6.2", "7.5"}


def test_internal_audit_section_matches_clause_9_2():
    section = Section(
        section_id="9.2.1",
        heading="Internal audit",
        body="The organization shall conduct internal audits and report the results.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "9.2"


def test_management_review_section_matches_clause_9_3():
    section = Section(
        section_id="9.3.1",
        heading="Management review",
        body="Top management shall review the environmental management system.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "9.3"


def test_corrective_action_section_matches_clause_10_2():
    section = Section(
        section_id="10.2.1",
        heading="Corrective action",
        body="The organization shall react to nonconformity and take corrective action.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "10.2"


def test_continual_improvement_section_matches_clause_10_3():
    section = Section(
        section_id="10.3.1",
        heading="Continual improvement",
        body="The organization shall continually improve the suitability, adequacy and effectiveness of the EMS.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "10.3"


