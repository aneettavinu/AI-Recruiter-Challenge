import os
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import create_candidate_text
from score import calculate_final_score
from skill_match import skill_match
from explain import generate_reason
from job_parser import extract_job_requirements

# -----------------------------
# Create Output Folder
# -----------------------------
os.makedirs("output", exist_ok=True)

# -----------------------------
# Load Model
# -----------------------------
print("=" * 60)
print("Loading Sentence Transformer Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Read Job Description
# -----------------------------
print("Reading Job Description...")

job = extract_job_requirements("data/job_description.docx")

job_text = job["job_text"]
required_skills = job["required_skills"]

print("\nRequired Skills:")
print(required_skills)

job_embedding = model.encode(job_text)

# -----------------------------
# Read Candidates
# -----------------------------
results = []

LIMIT = None      # Change to None later for full dataset

print("\nProcessing Candidates...\n")

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for index, line in enumerate(file):

        if LIMIT is not None and index >= LIMIT:
            break

        candidate = json.loads(line)

        candidate_text = create_candidate_text(candidate)

        candidate_embedding = model.encode(candidate_text)

        similarity = cosine_similarity(
            [job_embedding],
            [candidate_embedding]
        )[0][0]

        skill_score = skill_match(
            candidate,
            required_skills
        )

        final_score = calculate_final_score(
            similarity,
            candidate
        )

        final_score += skill_score * 20

        reason = generate_reason(
            candidate,
            similarity,
            skill_score
        )

        results.append({

            "candidate_id":
                candidate["candidate_id"],

            "candidate_name":
                candidate["profile"]["anonymized_name"],

            "similarity":
                round(similarity, 4),

            "skill_score":
                round(skill_score * 20, 2),

            "experience":
                candidate["profile"]["years_of_experience"],

            "github_score":
                candidate["redrob_signals"]["github_activity_score"],

            "final_score":
                round(final_score, 2),

            "reason":
                reason

        })

# -----------------------------
# Ranking
# -----------------------------
df = pd.DataFrame(results)

df = df.sort_values(
    by="final_score",
    ascending=False
)

df.reset_index(drop=True, inplace=True)

df["rank"] = df.index + 1

# -----------------------------
# Display Top 20
# -----------------------------
print("\nTop 20 Candidates\n")
print(df.head(20))

# -----------------------------
# Save CSV
# -----------------------------
output_file = "output/top_candidates.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("Ranking Completed Successfully")
print(f"Saved File : {output_file}")
print("=" * 60)