from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section
from iso14001_rules_check_tools.reporter import render_section_report


def test_match_section_returns_environmental_policy_for_section():
    section = Section(
        section_id="2",
        heading="Environmental policy",
        body="The organization shall establish an environmental policy and communicate it.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.2"


def test_text_report_includes_top_match_summary():
    section = Section(
        section_id="6.1.3.1",
        heading="Compliance obligations",
        body="The organization shall determine compliance obligations and keep them current.",
    )

    output = render_section_report((section,))

    assert "Top match:" in output
    assert "6.1.3" in output
