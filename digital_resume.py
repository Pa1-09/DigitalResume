from pathlib import Path
from PIL import Image
import streamlit as st
import pandas as pd
from assets.projects import projects

# ------ Path Settings -------
# getting the parent folder of digital_resume python file
if "__file__" in locals():
    current_dir = Path(__file__).parent
else:
    current_dir = Path.cwd()

css_file = Path(current_dir, "styles", "main.css")

# Resume to be modified
resume_file = Path(current_dir, "assets", "Pavan_Python_Django.pdf")
profile_pic = Path(current_dir, "assets", "profile-picsmall2.png")


# ------ General Settings ----------
PAGE_TITLE = "Digital Resume | Pavan A"
PAGE_ICON = "👋"
NAME = "Pavan Kumar Andalavari"

PATH = Path(current_dir, "assets", "job_profile.txt")

SKILLS_PATH = Path(current_dir, "assets", "skills.txt")

COMPANIES_LIST = Path(current_dir, "assets", "companies.csv")

# PROJECTS_DATA = Path(current_dir, "assets", "projects.py")


with open(PATH, "r") as f:
        JOB_PROFILE = f.readlines()

with open(SKILLS_PATH, "r") as sp:
    SKILLS = sp.readlines()

    with open(COMPANIES_LIST, "r") as cl:
        COMPANY_PROFILE = cl.readlines()

EMAIL = "pavankumar.andalavari@gmail.com"
PHONE = "+91- 9398346627"
SOCIAL_MEDIA_LINKS = {
    "GitHub" : "https://github.com/Pa1-09/",

    # link to be modified
    "Linkedin" : "https://in.linkedin.com/"

}

# to be decided and added later on
PROJECTS = {
    # Project name : Description
    "Digital_Resume" : "https://pa1-09-digitalresume-digital-resume-43rkuj.streamlit.app/",
    "Weather_Predictor" : "https://github.com/Pa1-09/Weather_Forecast_Project",
    "Order_Service": "https://github.com/Pa1-09/ServiceAppNag"

}


# Real work starts here
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF, Profile Pic
with open(css_file, "r") as css:
    css_f = css.read()
    st.markdown(f"<style>{css_f}</style>",unsafe_allow_html=True)

with open(resume_file, "rb") as pdf:
    pdf_content = pdf.read()

profile_picture = Image.open(profile_pic)


# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_picture, width=200)

with col2:
    st.subheader(NAME)
    st.write("Python and Django Developer.")
    st.write("Manual and Automation Tester.")

st.write("---")

col4, col5, col6 = st.columns([1,2,2], gap="small")
with col4:
    st.write(" Phone: :telephone_receiver:", PHONE)

with col5:
    st.write("Email: :email:", EMAIL)

with col6:
    st.download_button(
        label=":point_right: Download Resume(PDF)",
        data = pdf_content,
        file_name=resume_file.name,
    )

st.write("---")

# Displaying social media links
all_social_links = st.columns(len(SOCIAL_MEDIA_LINKS))
for index, (social_media_name, social_link) in enumerate(SOCIAL_MEDIA_LINKS.items()):
    all_social_links[index].write(f"[{social_media_name}]({social_link})")
st.write("---")

# Displaying experience and qualifications

st.subheader("Experience and Qualifications")
for exp_profile in JOB_PROFILE:
        st.write(f"- {exp_profile}")


# Displaying skills
st.write("#")
st.subheader("Skills")

for each_skill in SKILLS:
        st.write(f"- {each_skill}")


# companies
st.subheader("Professional Work Experience ")
df = pd.read_csv(COMPANIES_LIST)
st.write((df.loc[:,: ]))



# ---- work history ----- to be written here
st.subheader("Work history")

st.write("Project 4 Description:")
st.write(projects["project4_description"])
st.write("\n")
st.write("Project 4  Contribution:")
st.write(projects['project4_contribution'])
st.write("\n")
st.write("Project 4  TechStack:")
st.write(projects['project4_techstack'])

st.write(3*"\n")

st.write("Project 3 Description:")
st.write(projects["project3_description"])
st.write("\n")
st.write("Project 3  Contribution:")
st.write(projects['project3_contribution'])
st.write("\n")
st.write("Project 3  TechStack:")
st.write(projects['project3_techstack'])

st.write(3*"\n")

st.write("Project 2 Description:")
st.write(projects["project2_description"])
st.write("\n")
st.write("Project 2  Contribution:")
st.write(projects['project2_contribution'])
st.write("\n")
st.write("Project 2  TechStack:")
st.write(projects['project2_techstack'])

st.write(3*"\n")

st.write("Project 1 Description: ")
st.write(projects["project1_description"])
st.write("\n")
st.write("Project 1  Contribution:")
st.write(projects['project1_contribution'])
st.write("\n")
st.write("Project 1  TechStack:")
st.write(projects['project1_techstack'])




# Projects and Acoomplishments
st.subheader("Other Projects")
# Displaying social media links
all_project_links = st.columns(len(PROJECTS))
for index, (project_name, project_link) in enumerate(PROJECTS.items()):
    all_project_links[index].write(f"[{project_name}]({project_link})")
st.write("---")


