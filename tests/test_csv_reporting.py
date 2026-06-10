from io import StringIO
import csv

from iso14001_rules_check_tools.models import Section
from iso14001_rules_check_tools.reporter import render_section_report_csv


def test_render_section_report_csv_outputs_header_and_match_rows():
    sections = (
        Section(
            section_id="2",
            heading="Environmental policy",
            body="The organization shall establish an environmental policy and communicate it.",
        ),
    )

    csv_text = render_section_report_csv(sections)
    rows = list(csv.DictReader(StringIO(csv_text)))

    assert rows[0]["section_id"] == "2"
    assert rows[0]["clause_id"] == "5.2"
    assert rows[0]["matched_keywords"]
    assert "keywords:" in rows[0]["reason"] or "title hit:" in rows[0]["reason"]


def test_render_section_report_csv_keeps_sections_without_matches():
    sections = (
        Section(
            section_id="9.9",
            heading="Anything",
            body="No clause keywords here.",
        ),
    )

    csv_text = render_section_report_csv(sections)
    rows = list(csv.DictReader(StringIO(csv_text)))

    assert len(rows) == 1
    assert rows[0]["section_id"] == "9.9"
    assert rows[0]["match_rank"] == "0"
    assert rows[0]["clause_id"] == ""
