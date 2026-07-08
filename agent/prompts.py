ANALYSIS_PROMPT = """You are a Senior Business Analyst reviewing a user story.

User Story:
{story}

Analyze it for clarity, completeness, and quality using INVEST principles
(Independent, Negotiable, Valuable, Estimable, Small, Testable).

Provide:
1. A short quality assessment (2-3 sentences)
2. An improved/rewritten version of the user story if needed
"""

ACCEPTANCE_CRITERIA_PROMPT = """Based on this user story:
{story}

Generate 4-6 clear Acceptance Criteria in Given/When/Then format.
"""

TEST_CASES_PROMPT = """Based on this user story:
{story}

Generate:
- 3 positive test cases (expected/valid flow)
- 3 negative test cases (invalid input, edge cases, errors)

Format as a numbered list with short titles and expected results.
"""

RISK_PROMPT = """Based on this user story:
{story}

Identify 3-5 potential risks (technical, business, or usability) related to
implementing this feature. For each risk, provide a short mitigation suggestion.
"""

RECOMMENDATIONS_PROMPT = """Based on the full analysis of this user story:
{story}

Provide 3 short, actionable recommendations for the development team.
"""