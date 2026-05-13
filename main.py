import streamlit as st
import fitz
import json
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Initialize Client
client = Groq(api_key=api_key)

#UI Configuration 
st.set_page_config(page_title="AI CV Analyzer Pro", layout="wide")

# Custom CSS for better look
st.markdown("""
    <style>
    .skill-tag {
        display: inline-block;
        padding: 4px 12px;
        margin: 4px;
        border-radius: 15px;
        background-color: #1e3a8a;
        color: white;
        font-size: 14px;
    }
    .missing-tag {
        display: inline-block;
        padding: 4px 12px;
        margin: 4px;
        border-radius: 15px;
        background-color: #7f1d1d;
        color: white;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

def extract_text_from_pdf(uploaded_file):
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text().strip()
    return text

# Sidebar
st.sidebar.title("Settings")
job_desc = st.sidebar.text_area("Target Job Description:", placeholder="Paste the job requirements here...", height=300)

#  Main App
st.title("Smart CV Analyzer")
st.write("Upload your resume and get instant AI feedback on your job fit.")

uploaded_file = st.file_uploader("Choose your Resume (PDF)", type="pdf")

if uploaded_file and job_desc:
    if st.button("Analyze My Resume"):
        with st.spinner('AI is processing your profile...'):
            try:
                # 1. Extraction
                resume_text = extract_text_from_pdf(uploaded_file)
                
                # 2. AI Request
                prompt = f"""
                Resume: {resume_text}
                Job: {job_desc}
                Task: Analyze the resume against the job description.
                Return ONLY a JSON with keys: 
                'match_score' (integer), 'summary' (string), 'skills' (list of strings), 'missing_skills' (list of strings).
                """
                
                completion = client.chat.completions.create(
                    model='llama-3.1-8b-instant',
                    messages=[
                        {"role": "system", "content": "You are a professional HR assistant. Output ONLY JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={'type': "json_object"}
                )
                
                results = json.loads(completion.choices[0].message.content)

                # 3. Visualizing Results
                st.balloons()
                
                # Score Metric
                score = results.get('match_score', 0)
                st.markdown(f"## Match Score: {score}%")
                st.progress(score / 100)
                
                st.divider()

                # Summary Section
                st.subheader("Professional Summary")
                st.info(results.get('summary'))

                # Skills Comparison Columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### Your Skills")
                    skills = results.get('skills', [])
                    if skills:
                        html_tags = "".join([f'<div class="skill-tag">{s}</div>' for s in skills])
                        st.markdown(html_tags, unsafe_allow_html=True)
                    else:
                        st.write("No specific skills found.")

                with col2:
                    st.markdown("### Missing Skills")
                    missing = results.get('missing_skills', [])
                    if missing:
                        html_tags = "".join([f'<div class="missing-tag">{m}</div>' for m in missing])
                        st.markdown(html_tags, unsafe_allow_html=True)
                    else:
                        st.success("You have all the required skills!")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
else:
    st.info("Waiting for your Resume and Job Description...")