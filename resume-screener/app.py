from fastapi import FastAPI, UploadFile, File
import os
from fastapi.middleware.cors import CORSMiddleware

from pdf_reader import extract_pdf_text
from skill_matcher import extract_skills_nlp
from scorer import score_resume
from semantic_matcher import semantic_similarity

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Resume Screener API Running"
    }


@app.post("/upload")
async def upload_resume(
    resume: UploadFile = File(...)
):
    filepath = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    with open(filepath, "wb") as f:
        f.write(await resume.read())

    return {
        "saved": resume.filename
    }


@app.post("/analyze")
async def analyze(
    jd: UploadFile = File(...),
    resume: UploadFile = File(...)
):

    # Read JD text
    jd_text = (
        await jd.read()
    ).decode("utf-8")

    # Save resume PDF
    resume_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    # Extract text from PDF
    resume_text = extract_pdf_text(
        resume_path
    )

    # Extract skills
    jd_skills = extract_skills_nlp(
        jd_text
    )

    resume_skills = extract_skills_nlp(
        resume_text
    )

    # Skill matching score
    score, matched, missing = score_resume(
        jd_skills,
        resume_skills
    )

    # Semantic score
    semantic_score = semantic_similarity(
        jd_text,
        resume_text
    )

    # Combined score
    final_score = (
        0.7 * score +
        0.3 * semantic_score
    )

    return {
        "final_score": round(final_score, 2),
        "skill_score": round(score, 2),
        "semantic_score": round(semantic_score, 2),
        "matched": matched,
        "missing": missing,
        "resume_skills": resume_skills
    }