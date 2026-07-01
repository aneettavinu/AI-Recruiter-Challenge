import pandas as pd
import os

os.makedirs("output", exist_ok=True)


def create_submission(input_file):

    df = pd.read_csv(input_file)

    # Sort by final score
    df = df.sort_values(
        by="final_score",
        ascending=False
    )

    df.reset_index(drop=True, inplace=True)

    # Rank
    df["rank"] = df.index + 1

    # Normalize score between 0 and 1
    max_score = df["final_score"].max()
    min_score = df["final_score"].min()

    if max_score == min_score:
        df["score"] = 1.0
    else:
        df["score"] = (
            (df["final_score"] - min_score)
            /
            (max_score - min_score)
        )

    submission = pd.DataFrame({

        "candidate_id": df["candidate_id"],

        "rank": df["rank"],

        "score": df["score"].round(3),

        "reasoning": df["reason"]

    })

    submission.to_csv(

        "output/submission.csv",

        index=False

    )

    print("\nSubmission saved successfully!")
    print(submission.head())


if __name__ == "__main__":

    create_submission("output/top_candidates.csv")