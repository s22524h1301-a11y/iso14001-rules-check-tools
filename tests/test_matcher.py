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
    assert "environmental policy" in matches[0].matched_keywords


def test_context_language_matches_clause_4_1():
    section = Section(
        section_id="4.1.1",
        heading="Context of the organization",
        body="The organization determines external and internal issues relevant to its purpose.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "4.1"


def test_scope_language_matches_clause_4_3():
    section = Section(
        section_id="4.3.1",
        heading="Scope of the EMS",
        body="The scope of the environmental management system considers boundaries and applicability.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "4.3"


def test_leadership_language_matches_clause_5_1():
    section = Section(
        section_id="5.1.1",
        heading="Leadership and commitment",
        body="Top management demonstrates leadership and commitment to the environmental management system.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.1"


def test_roles_language_matches_clause_5_3():
    section = Section(
        section_id="5.3.1",
        heading="Roles and responsibilities",
        body="Responsibilities and authorities are assigned and communicated within the organization.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.3"


def test_empty_catalog_returns_no_matches():
    section = Section(
        section_id="9.9",
        heading="Anything",
        body="No clause keywords here.",
    )

    matches = match_section(section, ())

    assert matches == ()


def test_policing_words_do_not_create_false_matches():
    section = Section(
        section_id="4.2",
        heading="Process note",
        body="Our policymaking process and document records are kept internally.",
    )

    matches = match_section(section, default_clause_catalog())

    assert [match.clause_id for match in matches] == ["7.5"]


def test_single_clear_keyword_match_is_kept_without_title_hit():
    section = Section(
        section_id="5.2.1",
        heading="Internal memo",
        body="policy",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "5.2"


def test_operational_controls_section_prefers_clause_8_1():
    section = Section(
        section_id="8.1.1",
        heading="Operational controls",
        body="The organization shall establish criteria for its processes, control outsourced processes, and review planned changes.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "8.1"


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


def test_applicable_requirements_section_matches_clause_6_1_3():
    section = Section(
        section_id="6.1.3.1",
        heading="Applicable requirements",
        body="The organization shall determine applicable requirements for its environmental aspects.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "6.1.3"


def test_planning_action_language_matches_clause_6_1_4():
    section = Section(
        section_id="6.1.4.1",
        heading="Planning action",
        body="The organization plans actions to address significant environmental aspects and compliance obligations.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "6.1.4"


def test_planning_actions_to_achieve_objectives_matches_clause_6_2_2():
    section = Section(
        section_id="6.2.2.1",
        heading="Planning actions to achieve environmental objectives",
        body="The organization defines responsibilities and time frames for planning actions to achieve environmental objectives.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "6.2.2"


def test_compliance_evaluation_language_matches_clause_9_1_2():
    section = Section(
        section_id="9.1.2.1",
        heading="Evaluation of compliance",
        body="The organization periodically assesses compliance with legal and other requirements.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "9.1.2"


def test_general_policy_language_does_not_trigger_clause_6_1_3():
    section = Section(
        section_id="6.1.3.false",
        heading="General policy review",
        body="The organization reviews policies and responsibilities each quarter.",
    )

    matches = match_section(section, default_clause_catalog())

    assert all(match.clause_id != "6.1.3" for match in matches)


def test_generic_process_language_does_not_trigger_clause_8_1():
    section = Section(
        section_id="8.1.false",
        heading="Process description",
        body="The team describes standard workflow steps and common operating practices.",
    )

    matches = match_section(section, default_clause_catalog())

    assert all(match.clause_id != "8.1" for match in matches)


def test_continual_improvement_section_matches_clause_10_3():
    section = Section(
        section_id="10.3.1",
        heading="Continual improvement",
        body="The organization shall continually improve the suitability, adequacy and effectiveness of the EMS.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "10.3"


def test_general_improvement_language_matches_clause_10_1():
    section = Section(
        section_id="10.1.1",
        heading="General improvement",
        body="The organization identifies opportunities for improvement and acts on them.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "10.1"


def test_resources_language_matches_clause_7_1():
    section = Section(
        section_id="7.1.1",
        heading="Resources and support",
        body="The organization provides personnel, infrastructure, and monitoring and measuring resources for the EMS.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.1"


def test_competence_language_matches_clause_7_2():
    section = Section(
        section_id="7.2.1",
        heading="Competence and training",
        body="Training needs are identified and competence records are retained for relevant personnel.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.2"


def test_awareness_language_matches_clause_7_3():
    section = Section(
        section_id="7.3.1",
        heading="Awareness",
        body="Employees are aware of the environmental policy, significant environmental aspects, and the implications of not conforming.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.3"


def test_internal_communication_language_matches_clause_7_4_2():
    section = Section(
        section_id="7.4.2.1",
        heading="Internal communication",
        body="Internal communication includes employee communication and internal briefings about EMS changes.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.4.2"


def test_external_communication_language_matches_clause_7_4_3():
    section = Section(
        section_id="7.4.3.1",
        heading="External communication",
        body="External reporting and regulatory communication are handled through the assigned process.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.4.3"


def test_documented_information_language_matches_clause_7_5():
    section = Section(
        section_id="7.5.1",
        heading="Control of documented information",
        body="Document control includes approval, version control, retention, access, and archive rules.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "7.5"


def test_emergency_preparedness_language_matches_clause_8_2():
    section = Section(
        section_id="8.2.1",
        heading="Emergency preparedness and response",
        body="The emergency plan covers spill response, evacuation, drills, and incident response for accidental releases.",
    )

    matches = match_section(section, default_clause_catalog())

    assert matches[0].clause_id == "8.2"


