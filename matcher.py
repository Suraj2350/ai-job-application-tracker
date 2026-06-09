from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def calculate_match_score(resume_text, job_description):
    """
    Compare resume text with job description and return a match score.
    Score will be between 0 and 100.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = similarity[0][0] * 100

    return round(score, 2)


def contains_skill(text, skill):
    """
    Check if a skill exists in text.
    Example: 'api' should match 'REST API', but not 'application'.
    """

    text = text.lower()
    skill = skill.lower()

    pattern = r"\b" + re.escape(skill) + r"\b"

    return re.search(pattern, text) is not None


def find_missing_keywords(resume_text, job_description):
    """
    Find important skill keywords from the job description
    that are missing in the resume.
    """

    important_skills = [
        "python",
        "java",
        "javascript",
        "typescript",
        "html",
        "css",
        "sql",
        "react",
        "node",
        "fastapi",
        "flask",
        "django",
        "api",
        "rest",
        "git",
        "github",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "gcp",
        "linux",
        "bash",
        "machine learning",
        "data analysis",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "testing",
        "pytest",
        "unit testing",
        "automation",
        "database",
        "postgresql",
        "mysql",
        "mongodb",
        "agile",
        "scrum",
        "security",
        "cloud",
    ]

    missing_skills = []

    for skill in important_skills:
        skill_in_job = contains_skill(job_description, skill)
        skill_in_resume = contains_skill(resume_text, skill)

        if skill_in_job and not skill_in_resume:
            missing_skills.append(skill)

    return missing_skills