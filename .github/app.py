import streamlit as st
from PIL import Image
import base64

# --- SETTINGS ---
PAGE_TITLE = "Chandrika Joshi | Data Scientist"
PAGE_ICON = "💡"
NAME = "Chandrika Joshi"
DESCRIPTION = """
Data Scientist | AI/ML Engineer | Freelancer | Blogger
"""
EMAIL = "Jchandrika67@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/yourprofile",
    "GitHub": "https://github.com/chandrikajoshi123",
    "Medium": "https://medium.com/@yourprofile"
}
PROJECTS = {
    "🏆 LLM Resume Reviewer": "Streamlit app using OpenAI GPT to analyze and improve resumes.",
    "🏆 Credit Card Fraud Detection": "Isolation Forest model (96% ROC-AUC) for anomaly detection.",
    "🏆 Sentiment Analysis API": "FastAPI model classifying Amazon reviews with 89% accuracy.",
    "🏆 Customer Churn Prediction": "Random Forest + Power BI dashboard to track churn drivers."
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD ASSETS ---
def img_to_bytes(img_path):
    img = Image.open(img_path)
    return base64.b64encode(img.getvalue()).decode()

profile_pic = Image.open("assets/profile.jpg")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    
    # Social media links
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# --- ABOUT ME ---
st.write("\n")
st.subheader("About Me")
st.write("""
- 🔭 Pursuing MSc in **Data Science & Statistics** at Graphic Era Hill University
- 🌱 Specializing in **LLMs, NLP, and Generative AI**
- ✍️ Blogging about AI, Python, and career growth on Medium
- 💡 Passionate about solving real-world problems with data
""")

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Programming**")
    st.write("- Python (Pandas, NumPy)")
    st.write("- SQL, R")

with col2:
    st.write("**Machine Learning**")
    st.write("- PyTorch, Scikit-learn")
    st.write("- NLP (BERT, GPT-3.5)")

with col3:
    st.write("**Tools**")
    st.write("- Git, Docker")
    st.write("- Power BI, AWS")

# --- PROJECTS ---
st.write("\n")
st.subheader("Projects")
for project, description in PROJECTS.items():
    st.write(f"**{project}**")
    st.write(f"- {description}")

# --- EXPERIENCE ---
st.write("\n")
st.subheader("Experience")
st.write("""
**👩‍💻 Data Science Intern | ZIDIO, India** (Feb 2025 - Apr 2025)
- Built Power BI dashboards improving KPI visibility by 30%
- Trained ML models boosting prediction accuracy by 15%

**👩‍💻 AI Intern | Coding Jr, India** (Jun 2024 - Sep 2024)
- Deployed LLM-based resume reviewer with 99% uptime
- Reduced inference latency by 12% using FastAPI
""")

# --- RESUME DOWNLOAD ---
st.write("\n")
st.subheader("Resume")
with open("assets/resume.pdf", "rb") as f:
    resume_bytes = f.read()
st.download_button(
    label="📄 Download Resume",
    data=resume_bytes,
    file_name="ChandrikaJoshi_Resume.pdf",
    mime="application/pdf"
)

# --- CONTACT ---
st.write("\n")
st.subheader("Contact Me")
contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@EMAIL.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Hide Streamlit branding
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)