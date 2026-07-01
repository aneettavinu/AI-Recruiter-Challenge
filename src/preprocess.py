import json


def create_candidate_text(candidate):

    profile = candidate["profile"]

    text = []

    # ---------------- Profile ----------------

    text.append(profile["headline"])
    text.append(profile["summary"])

    text.append(f"Experience: {profile['years_of_experience']} years")

    text.append(f"Current Title: {profile['current_title']}")

    text.append(f"Current Company: {profile['current_company']}")

    text.append(f"Industry: {profile['current_industry']}")

    # ---------------- Career ----------------

    text.append("\nCareer History")

    for job in candidate["career_history"]:
        text.append(
            f"{job['title']} at {job['company']}. {job['description']}"
        )

    # ---------------- Education ----------------

    text.append("\nEducation")

    for edu in candidate["education"]:
        text.append(
            f"{edu['degree']} in {edu['field_of_study']} from {edu['institution']}"
        )

    # ---------------- Skills ----------------

    text.append("\nSkills")

    for skill in candidate["skills"]:
        text.append(skill["name"])

    # ---------------- Certifications ----------------

    text.append("\nCertifications")

    for cert in candidate["certifications"]:
        text.append(cert["name"])

    # ---------------- Languages ----------------

    text.append("\nLanguages")

    for lang in candidate["languages"]:
        text.append(lang["language"])

    # ---------------- Redrob Signals ----------------

    signal = candidate["redrob_signals"]

    text.append("\nPlatform Signals")

    text.append(f"Open To Work: {signal['open_to_work_flag']}")

    text.append(f"GitHub Score: {signal['github_activity_score']}")

    text.append(
        f"Profile Completeness: {signal['profile_completeness_score']}"
    )

    return "\n".join(text)


if __name__ == "__main__":

    candidates = []

    with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
        for line in file:
            candidates.append(json.loads(line))

    profile_text = create_candidate_text(candidates[0])

    print(profile_text)