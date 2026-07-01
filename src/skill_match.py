def skill_match(candidate, required_skills):

    candidate_skills = {
        skill["name"].lower()
        for skill in candidate["skills"]
    }

    required = {
        skill.lower()
        for skill in required_skills
    }

    matched = candidate_skills.intersection(required)

    if len(required) == 0:
        return 0

    return len(matched) / len(required)