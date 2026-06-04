# Calculate skill match score between JD and resume

def score_resume(jd_skills, resume_skills):

    matched = []
    missing = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(jd_skills)) * 100

    return score, matched, missing


IMPORTANT_SKILLS = {
    "python": 10,
    "sql": 8,
    "aws": 10,
    "machine learning": 10,
    "docker": 5,
}

def weighted_score(
    jd_skills,
    resume_skills
):

    total_weight = 0
    matched_weight = 0

    for skill in jd_skills:

        weight = IMPORTANT_SKILLS.get(
            skill,
            3
        )

        total_weight += weight

        if skill in resume_skills:
            matched_weight += weight

    score = (
        matched_weight
        / total_weight
    ) * 100

    return score