import json
from sentence_transformers import SentenceTransformer
from preprocess import create_candidate_text

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    candidates = [json.loads(line) for line in file]

candidate = candidates[0]

text = create_candidate_text(candidate)

embedding = model.encode(text)

print(candidate["candidate_id"])
print(len(embedding))