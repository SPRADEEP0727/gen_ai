import streamlit as st
from analyzer import ResumeAnalyzer
from ui_custom import set_custom_background
from ui_custom import set_custom_title
import PyPDF2

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text


def main():
    st.set_page_config(
        
        page_title="ResumeGenius.ai - AI Resume Analyzer",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    #set_custom_background("ai_powered.jpg")
    set_custom_title()

    # --- Custom styles for labels ---
    st.markdown("""
        <style>
        .neon-label {
            font-size: 18px;
            font-weight: bold;
            color: black;
            margin-bottom: -16px;
            line-height: 1.0;
        }
        div[data-testid="stVerticalBlock"] > div {
            margin-top: -10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Select Industry ---
    st.markdown('<div class="neon-label">Which industry are you targeting?</div>', unsafe_allow_html=True)
    industry = st.selectbox("", tuple(ResumeAnalyzer.INDUSTRY_KEYWORDS.keys()), key="industry_select")

    # --- Input Job Role ---
    st.markdown('<div class="neon-label" style="margin-top: 20px;">What job role are you looking for?</div>', unsafe_allow_html=True)
    job_role = st.text_input("", placeholder="e.g., Data Analyst, Marketing Manager", key="job_role_input")

    # --- Upload Resume ---
    st.markdown('<div class="neon-label" style="margin-top: 20px;">Upload your resume (PDF only)</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["pdf"], key="resume_upload")

    

    if uploaded_file is not None:
        analyzer = ResumeAnalyzer(industry=industry)
        #insights = analyzer.analyze_resume(resume_text)

        #st.subheader("Analysis Results")
        #for insight in insights:
            #st.write(insight)


    # --- Columns for buttons ---
    col1, col2, col3 = st.columns([1, 1, 1])

    # --- Inject button styles ---
    st.markdown("""
        <style>
        .custom-button {
            display: inline-block;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            color: white;
            cursor: pointer;
            width: 100%;
            text-align: center;
            margin-top: 10px;
        }

        .btn-orange {
            background-color: #FF7F00;
        }

        .btn-naukri {
            background-color: #00468B;
        }

        .btn-linkedin {
            background-color: #0077B5;
        }

        .custom-button:hover {
            opacity: 0.7;
            transition: 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Buttons with JavaScript form triggers ---
    with col1:
        resume_btn = st.markdown("<button class='custom-button btn-orange'>Analyze Resume</button>", unsafe_allow_html=True)
        if st.button("▶️", key="trigger1"):  # Hidden trigger button
            gpt_result = analyzer.gpt_analysis(resume_text, industry)
            st.subheader("ResumeGenius.ai Analysis")
            st.write(gpt_result)

    with col2:
        naukri_btn = st.markdown("<button class='custom-button btn-naukri'>Analyze for Naukri</button>", unsafe_allow_html=True)
        if st.button("▶️", key="trigger2"):
            gpt_result = analyzer.gpt_analysis(resume_text, industry)
            st.subheader("Naukri-Focused Analysis")
            st.write(gpt_result)

    with col3:
        linkedin_btn = st.markdown("<button class='custom-button btn-linkedin'>Analyze for LinkedIn</button>", unsafe_allow_html=True)
        if st.button("▶️", key="trigger3"):
            gpt_result = analyzer.gpt_analysis(resume_text, industry)
            st.subheader("LinkedIn-Focused Analysis")
            st.write(gpt_result)





if __name__ == "__main__":
    main()