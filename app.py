import streamlit as st
from matcher import calculate_match_score, find_missing_keywords

st.set_page_config(page_title="AI Job Application Tracker", page_icon="📄")

st.title("AI Job Application Tracker")
st.write("This app compares your resume with a job description and gives a match score.")

resume_text = st.text_area("Paste your resume text here", height=200)

job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyze Match"):
    if resume_text.strip() and job_description.strip():
        score = calculate_match_score(resume_text, job_description)
        missing_keywords = find_missing_keywords(resume_text, job_description)

        st.success("Analysis complete!")

        st.subheader("Resume Match Score")
        st.metric(label="Match Score", value=f"{score}%")

        if score >= 75:
            st.write("Strong match. Your resume matches this job well.")
        elif score >= 50:
            st.write("Medium match. Your resume has some relevant skills, but can be improved.")
        else:
            st.write("Low match. You may need to add more relevant skills or experience.")

        st.subheader("Missing Keywords")

        if len(missing_keywords) > 0:
            st.write("These important skills appear in the job description but not in your resume:")

            for keyword in missing_keywords:
                st.write(f"- {keyword}")

            st.subheader("Suggestions")

            for keyword in missing_keywords:
                st.write(f"- Consider adding a project, skill, or experience related to {keyword}.")
        else:
            st.write("No major missing keywords found.")

    else:
        st.warning("Please enter both resume text and job description.")