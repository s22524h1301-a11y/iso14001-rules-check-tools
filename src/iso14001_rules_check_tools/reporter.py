from __future__ import annotations

import csv
import json
from io import StringIO
from typing import cast

from iso14001_rules_check_tools.clause_catalog import default_clause_catalog
from iso14001_rules_check_tools.matcher import match_section
from iso14001_rules_check_tools.models import Section


def build_section_report(sections: tuple[Section, ...]) -> dict[str, object]:
    catalog = default_clause_catalog()
    section_entries: list[dict[str, object]] = []
    for section in sections:
        matches = match_section(section, catalog)
        section_entries.append(
            {
                "section_id": section.section_id,
                "heading": section.heading,
                "body": section.body,
                "matches": [
                    {
                        "clause_id": match.clause_id,
                        "clause_title": match.clause_title,
                        "score": match.score,
                        "matched_keywords": list(match.matched_keywords),
                        "reason": match.reason,
                    }
                    for match in matches
                ],
            }
        )
    return {"format": "report", "sections": section_entries}


def render_section_report(sections: tuple[Section, ...]) -> str:
    report = build_section_report(sections)
    section_entries = cast(list[dict[str, object]], report["sections"])
    lines: list[str] = []
    for section in section_entries:
        lines.append(f"[{section['section_id']}] {section['heading']}")
        if section["body"]:
            lines.append(cast(str, section["body"]))
        matches = cast(list[dict[str, object]], section["matches"])
        if matches:
            lines.append("Matches:")
            for match in matches:
                lines.append(f"- {match['clause_id']} {match['clause_title']}")
                lines.append(f"  {match['reason']}")
        else:
            lines.append("Matches: none")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_section_report_json(sections: tuple[Section, ...]) -> str:
    report = build_section_report(sections)
    report["format"] = "json"
    return json.dumps(report, ensure_ascii=False, indent=2)


def render_section_report_csv(sections: tuple[Section, ...]) -> str:
    catalog = default_clause_catalog()
    buffer = StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=(
            "section_id",
            "heading",
            "body",
            "match_rank",
            "clause_id",
            "clause_title",
            "score",
            "matched_keywords",
            "reason",
        ),
    )
    writer.writeheader()
    for section in sections:
        matches = match_section(section, catalog)
        if matches:
            for match_rank, match in enumerate(matches, start=1):
                writer.writerow(
                    {
                        "section_id": section.section_id,
                        "heading": section.heading,
                        "body": section.body,
                        "match_rank": match_rank,
                        "clause_id": match.clause_id,
                        "clause_title": match.clause_title,
                        "score": match.score,
                        "matched_keywords": "; ".join(match.matched_keywords),
                        "reason": match.reason,
                    }
                )
        else:
            writer.writerow(
                {
                    "section_id": section.section_id,
                    "heading": section.heading,
                    "body": section.body,
                    "match_rank": 0,
                    "clause_id": "",
                    "clause_title": "",
                    "score": 0,
                    "matched_keywords": "",
                    "reason": "No keyword overlap",
                }
            )
    return buffer.getvalue()
