from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(
    text1,
    text2
):
    emb1 = model.encode([text1])

    emb2 = model.encode([text2])

    score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    return float(round(score * 100, 2))


jd = """
Looking for experience in
Machine Learning and AI
"""

resume = """
Built Deep Learning systems
using PyTorch and TensorFlow
"""

print(
    semantic_similarity(
        jd,
        resume
    )
)