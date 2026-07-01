import pandas as pd


def rank_candidates(df):

    df = df.sort_values(
        by="final_score",
        ascending=False
    )

    df["rank"] = range(
        1,
        len(df)+1
    )

    return df


if __name__ == "__main__":

    df = pd.read_csv("output/top_candidates.csv")

    ranked = rank_candidates(df)

    ranked.to_csv(
        "output/ranked_candidates.csv",
        index=False
    )

    print(ranked.head(20))

    print("\nRanking Completed Successfully.")