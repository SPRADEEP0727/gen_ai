import streamlit as st
import base64
from analyzer import ResumeAnalyzer

def set_custom_background(image_path: str):
    """Set a custom background image for the Streamlit app."""
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_custom_title():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">

        <style>
        .title-container {
            text-align: center;
            margin-bottom: 5px;
        }

        .title-glow {
            font-size: 60px;
            font-weight: bold;
            color: #00FFFF;
            font-family: 'Orbitron', sans-serif;
            text-shadow:
                0 0 1px #00FFFF,
                0 0 3px #00FFFF,
                0 0 5px #00FFFF;
        }
        </style>

        <div class="title-container">
            <span class="title-glow">ResumeGenius.ai</span>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <p style='text-align:center; 
            color:lightgray;
            font-size:20px; 
            margin-bottom: 40px;'>
            Optimize Your Resume. Impress Every Recruiter
        </p>
    """, unsafe_allow_html=True)

    