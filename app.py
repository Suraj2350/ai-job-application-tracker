import streamlit as st
import pandas as pd
from matcher import calculate_match_score, find_missing_keywords
from database import (
    create_table,
    add_application,
    get_applications,
    delete_application,
    update_application_status,
)
from file_reader import extract_text_from_file

st.set_page_config(
    page_title="AI Job Application Tracker",
    page_icon="📄",
    layout="wide",
)

create_table()

st.sidebar.title("📄 AI Job Tracker")
st.sidebar.write("Track applications and improve your resume match.")

st.sidebar.markdown("### Features")
st.sidebar.write("✅ Resume match score")
st.sidebar.write("✅ Missing skills")
st.sidebar.write("✅ Job tracker")
st.sidebar.write("✅ Dashboard")
st.sidebar.write("✅ Update and delete applications")

st.title("📄 AI Job Application Tracker")
st.write(
    "Compare your resume with job descriptions, identify missing skills, "
    "and track your job applications in one place."
)

st.info(
    "Tip: Paste your resume and job description first, then click Analyze Match. "
    "After that, save the job application below."
)


st.subheader("Resume Input")

resume_file = st.file_uploader(
    "Upload your resume as a PDF or TXT file",
    type=["pdf", "txt"],
    key="resume_uploader",
)

uploaded_resume_text = extract_text_from_file(resume_file)

resume_text = st.text_area(
    "Or paste your resume text here",
    value=uploaded_resume_text,
    height=200,
)

st.subheader("Job Description Input")

job_file = st.file_uploader(
    "Upload the job description as a PDF or TXT file",
    type=["pdf", "txt"],
    key="job_uploader",
)

uploaded_job_text = extract_text_from_file(job_file)

job_description = st.text_area(
    "Or paste the job description here",
    value=uploaded_job_text,
    height=200,
)

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

        st.session_state["latest_score"] = score

    else:
        st.warning("Please enter both resume text and job description.")

        


st.divider()


st.header("Save Job Application")

company = st.text_input("Company Name")
job_title = st.text_input("Job Title")
status = st.selectbox(
    "Application Status",
    ["Interested", "Applied", "Interview", "Rejected", "Offer"],
)
notes = st.text_area("Notes")

latest_score = st.session_state.get("latest_score", 0)

if st.button("Save Application"):
    if company.strip() and job_title.strip():
        add_application(company, job_title, status, latest_score, notes)
        st.success("Job application saved!")
    else:
        st.warning("Please enter company name and job title.")
        
        st.header("Application Dashboard")

applications = get_applications()

if applications:
    df = pd.DataFrame(
        applications,
        columns=["ID", "Company", "Job Title", "Status", "Match Score", "Notes"],
    )

    total_applications = len(df)
    average_score = df["Match Score"].mean()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Applications", total_applications)

    with col2:
        st.metric("Average Match Score", f"{average_score:.2f}%")

    status_counts = df["Status"].value_counts()

    st.subheader("Applications by Status")
    st.bar_chart(status_counts)
else:
    st.write("No application data yet.")



st.divider()

st.header("Saved Job Applications")

applications = get_applications()

if applications:
    for application in applications:
        app_id = application[0]
        company_name = application[1]
        saved_job_title = application[2]
        saved_status = application[3]
        saved_score = application[4]
        saved_notes = application[5]

        st.write(f"**{company_name} — {saved_job_title}**")
        st.write(f"Status: {saved_status}")
        st.write(f"Match Score: {saved_score}%")

        if saved_notes:
            st.write(f"Notes: {saved_notes}")

        status_options = ["Interested", "Applied", "Interview", "Rejected", "Offer"]

        selected_status = st.selectbox(
            "Update Status",
            status_options,
            index=status_options.index(saved_status),
            key=f"status_{app_id}",
        )

        if st.button("Update Status", key=f"update_{app_id}"):
            update_application_status(app_id, selected_status)
            st.success("Status updated!")
            st.rerun()


   

        if st.button("Delete", key=f"delete_{app_id}"):
            delete_application(app_id)
            st.success("Application deleted. Refreshing...")
            st.rerun()

        st.write("---")
else:
    st.write("No saved applications yet.")