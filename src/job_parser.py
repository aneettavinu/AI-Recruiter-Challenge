import re
from read_job import read_job_description


def extract_job_requirements(file_path):

    job_text = read_job_description(file_path)

    skills_database = [

        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Spark",
        "AWS",
        "Azure",
        "GCP",
        "TensorFlow",
        "PyTorch",
        "Docker",
        "Kubernetes",
        "Airflow",
        "Kafka",
        "Databricks",
        "Snowflake",
        "Power BI",
        "Tableau",
        "Git",
        "Linux",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "FastAPI",
        "Flask",
        "Django"

    ]

    required_skills = []

    for skill in skills_database:

        if re.search(rf"\b{re.escape(skill)}\b", job_text, re.IGNORECASE):
            required_skills.append(skill)

    return {

        "job_text": job_text,

        "required_skills": required_skills

    }


if __name__ == "__main__":

    job = extract_job_requirements(
        "data/job_description.docx"
    )

    print(job["required_skills"])