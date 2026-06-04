from skill_matcher import extract_skills_nlp

text = """
Experienced Python developer.

Worked with SQL,
AWS,
Docker,
Machine Learning.
"""

print(
    extract_skills_nlp(text)
)