import streamlit as st
from analyzer import ResumeAnalyzer
import PyPDF2

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def main():
    st.title("Resume Analyzer")
    st.write("Upload your resume in PDF format for analysis.")

    industry = st.selectbox(
        "Select your industry",
        tuple(ResumeAnalyzer.INDUSTRY_KEYWORDS.keys())
    )

    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
    
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.text_area("Resume Text", resume_text, height=300)

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