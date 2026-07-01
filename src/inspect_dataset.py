import json

# Load the first candidate from the JSONL file
with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    first_candidate = json.loads(next(file))

print("=" * 60)
print("DATASET INSPECTION")
print("=" * 60)

# Top-level keys
print("\nTop-Level Keys:")
print(first_candidate.keys())

# Candidate ID
print("\nCandidate ID:")
print(first_candidate["candidate_id"])

# Profile Information
print("\nPROFILE")
for key, value in first_candidate["profile"].items():
    print(f"{key}: {value}")

# Career History
print("\nCAREER HISTORY")
for i, job in enumerate(first_candidate["career_history"], start=1):
    print(f"\nJob {i}")
    for key, value in job.items():
        print(f"{key}: {value}")

# Education
print("\nEDUCATION")
for i, edu in enumerate(first_candidate["education"], start=1):
    print(f"\nEducation {i}")
    for key, value in edu.items():
        print(f"{key}: {value}")

# Skills
print("\nSKILLS")
for skill in first_candidate["skills"]:
    print(
        f"{skill['name']} | "
        f"Proficiency: {skill['proficiency']} | "
        f"Endorsements: {skill['endorsements']}"
    )

# Certifications
print("\nCERTIFICATIONS")
if first_candidate["certifications"]:
    for cert in first_candidate["certifications"]:
        print(cert)
else:
    print("No Certifications")

# Languages
print("\nLANGUAGES")
for lang in first_candidate["languages"]:
    print(f"{lang['language']} ({lang['proficiency']})")

# Redrob Signals
print("\nREDROB SIGNALS")
for key, value in first_candidate["redrob_signals"].items():
    print(f"{key}: {value}")

print("\n" + "=" * 60)
print("Dataset inspection completed successfully.")
print("=" * 60)