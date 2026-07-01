import subprocess

print("=" * 60)
print("AI Candidate Ranking System")
print("=" * 60)

print("\nStep 1: Ranking Candidates...")
subprocess.run(["python", "src/candidate_ranker.py"])

print("\nStep 2: Creating Submission...")
subprocess.run(["python", "src/submission.py"])

print("\nPipeline Completed Successfully!")
print("Check the output folder for results.")