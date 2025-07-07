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
    set_custom_background("ai_powered.jpg")
    set_custom_title()

    # Neon label and tight layout for selectbox
    st.markdown("""
        <style>
        .neon-label {
            font-size: 18px;
            font-weight: bold;
            color: #00FFFF;
            margin-bottom: -14px;
            line-height: 1.0;
        }
        div[data-testid="stVerticalBlock"] > div {
            margin-top: -10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Neon industry label
    st.markdown('<div class="neon-label">Select your industry</div>', unsafe_allow_html=True)
    industry = st.selectbox("", tuple(ResumeAnalyzer.INDUSTRY_KEYWORDS.keys()), key="industry_select")

    # Neon upload label
    st.markdown('<div class="neon-label" style="margin-top: 20px;">Upload your resume (PDF only)</div>', unsafe_allow_html=True)
    # Inject custom CSS to style uploaded file name and size

    uploaded_file = st.file_uploader("", type=["pdf"], key="resume_upload")
    

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        # Custom colored label (light neon style)
        st.markdown("""
            <div style="font-size: 18px; font-weight: bold; color: #00FFFF; margin-bottom: -10px;">
                Resume Text
            </div>
        """, unsafe_allow_html=True)
        st.text_area("", resume_text, height=300)


        analyzer = ResumeAnalyzer(industry=industry)
        insights = analyzer.analyze_resume(resume_text)

        st.subheader("Analysis Results")
        for insight in insights:
            st.write(insight)

        if st.button("Analyze with GPT"):
            with st.spinner("GPT is analyzing..."):
                gpt_result = analyzer.gpt_analysis(resume_text, industry)
                st.subheader("GPT Analysis")
                st.write(gpt_result)

if __name__ == "__main__":
    main()