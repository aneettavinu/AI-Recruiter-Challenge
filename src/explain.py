def generate_reason(candidate, similarity, skill_score):
    """
    Generate an explanation for why the candidate received the score.
    """

    reasons = []

    # Semantic Match
    if similarity >= 0.80:
        reasons.append("Excellent semantic match with the job description")
    elif similarity >= 0.65:
        reasons.append("Good semantic match with the job description")
    else:
        reasons.append("Partial semantic match with the job description")

    # Skill Match
    if skill_score >= 0.80:
        reasons.append("Matches most of the required technical skills")
    elif skill_score >= 0.50:
        reasons.append("Matches several required technical skills")

    # Experience
    experience = candidate["profile"]["years_of_experience"]

    if experience >= 8:
        reasons.append(f"{experience:.1f} years of strong industry experience")
    elif experience >= 5:
        reasons.append(f"{experience:.1f} years of relevant experience")
    elif experience >= 2:
        reasons.append(f"{experience:.1f} years of professional experience")

    # Open to Work
    if candidate["redrob_signals"]["open_to_work_flag"]:
        reasons.append("Currently open to new opportunities")

    # GitHub Activity
    github = candidate["redrob_signals"]["github_activity_score"]

    if github >= 80:
        reasons.append("Highly active GitHub profile")
    elif github >= 50:
        reasons.append("Moderately active GitHub profile")

    # Profile Completeness
    completeness = candidate["redrob_signals"]["profile_completeness_score"]

    if completeness >= 90:
        reasons.append("Excellent profile completeness")
    elif completeness >= 70:
        reasons.append("Well-maintained professional profile")

    return "; ".join(reasons)