# Create skill dictionary and function to extract skills from text

SKILLS = [
    "python",
    "sql",
    "aws",
    "machine learning",
    "docker",
    "git",
    "java",
    "react",
]

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found