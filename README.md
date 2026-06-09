# AI Job Application Tracker

AI Job Application Tracker is a Python web app that compares a resume with a job description, gives a match score, identifies missing skills, and helps users track job applications.

## Features

- Paste resume text and job description
- Calculate resume match score using TF-IDF and cosine similarity
- Show missing technical keywords from the job description
- Give improvement suggestions based on missing skills
- Save job applications using SQLite
- View saved job applications
- Update application status
- Delete saved applications
- View dashboard with total applications, average match score, and status chart

## Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- SQLite
- Git/GitHub

## Project Structure

```text
ai-job-application-tracker/
│
├── app.py
├── matcher.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```
