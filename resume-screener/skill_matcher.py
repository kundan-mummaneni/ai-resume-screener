import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(
    nlp.vocab,
    attr="LOWER"
)

SKILLS = [
    "python",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "git",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "java",
    "react",
    "node.js",
    "mongodb",
]

patterns = [
    nlp.make_doc(skill)
    for skill in SKILLS
]

matcher.add(
    "SKILLS",
    patterns
)

def extract_skills_nlp(text):

    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:

        skill = doc[start:end].text.lower()

        found_skills.add(skill)

    return list(found_skills)