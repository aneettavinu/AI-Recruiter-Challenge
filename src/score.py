def calculate_final_score(similarity, candidate):

    # ---------------- Experience ----------------

    experience = candidate["profile"]["years_of_experience"]

    experience_score = min(experience * 2, 20)

    # ---------------- GitHub ----------------

    github = candidate["redrob_signals"]["github_activity_score"]

    if github < 0:
        github = 0

    github_score = github * 0.05

    # ---------------- Open to Work ----------------

    open_score = 5 if candidate["redrob_signals"]["open_to_work_flag"] else 0

    # ---------------- Profile Completeness ----------------

    profile_score = (
        candidate["redrob_signals"]["profile_completeness_score"]
        * 0.05
    )

    # ---------------- Semantic Score ----------------

    semantic_score = similarity * 70

    final_score = (
        semantic_score
        + experience_score
        + github_score
        + profile_score
        + open_score
    )

    return round(final_score, 2)