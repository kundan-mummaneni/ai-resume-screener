import os

from pdf_reader import extract_pdf_text
from skill_matcher import extract_skills_nlp
from scorer import score_resume
from scorer import weighted_score
from semantic_matcher import semantic_similarity

# Read JD

with open(r"resume-screener\sample_jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

jd_skills = extract_skills_nlp(jd_text)

print("JD Skills:")
print(jd_skills)

resume_folder = r"resume-screener\resumes"

files = os.listdir(resume_folder)

results = []

for file in files:

    if not file.lower().endswith(".pdf"):
        continue

    path = os.path.join(resume_folder, file)

    resume_text = extract_pdf_text(path)

    resume_skills = extract_skills_nlp(
        resume_text
    )

    _, matched, missing = score_resume(
    jd_skills,
    resume_skills
    )

    score = weighted_score(
    jd_skills,
    resume_skills
    )

    semantic_score = semantic_similarity(
    jd_text,
    resume_text
    )

    final_score = (
    0.7 * score
    + 0.3 * semantic_score
    )

    results.append({
    "name": file,
    "skill_score": score,
    "semantic_score": semantic_score,
    "final_score": final_score,
    "matched": matched,
    "missing": missing
})

# Sort results

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nCandidate Ranking\n")

for candidate in results:

    print()

    print(candidate["name"])

    print(
        f"Skill Score: "
        f"{candidate['skill_score']:.2f}"
    )

    print(
        f"Semantic Score: "
        f"{candidate['semantic_score']:.2f}"
    )

    print(
        f"Final Score: "
        f"{candidate['final_score']:.2f}"
    ) 