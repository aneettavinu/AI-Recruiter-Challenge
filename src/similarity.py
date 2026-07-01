import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import create_candidate_text
from read_job import read_job_description

model = SentenceTransformer("all-MiniLM-L6-v2")

job = read_job_description("data/job_description.docx")

job_embedding = model.encode(job)

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    candidates = [json.loads(line) for line in file]

candidate = candidates[0]

candidate_text = create_candidate_text(candidate)

candidate_embedding = model.encode(candidate_text)

score = cosine_similarity(
    [job_embedding],
    [candidate_embedding]
)[0][0]

print(candidate["candidate_id"])
print("Similarity:", score)