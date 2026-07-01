import json
import pandas as pd


def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":

    file_path = "data/candidates.jsonl"

    candidates = load_candidates(file_path)

    print("Total Candidates :", len(candidates))

    print("\nFirst Candidate ID:")

    print(candidates[0]["candidate_id"])