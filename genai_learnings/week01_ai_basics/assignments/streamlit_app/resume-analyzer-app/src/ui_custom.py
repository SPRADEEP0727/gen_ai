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
        <style>
            /* Full-width navbar (independent of Streamlit container) */
            .custom-navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                background-color: #ffffff;
                padding: 16px 200px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                display: flex;
                align-items: center;
                justify-content: space-between;
                border-bottom: 1px solid #eee;
                z-index: 999;
            }

            .custom-navbar .left {
                font-size: 30px;
                font-weight: bold;
                color: #2563EB;
                font-family: 'Segoe UI', sans-serif;

            }

            .custom-navbar .right a {
                margin-left: 24px;
                text-decoration: none;
                font-size: 18px;
                color: #1f2937;
                font-family: 'Segoe UI', sans-serif;
            }

            .custom-navbar .right a.register {
                background-color: #EF4444;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: 600;
            }

            /* Add padding to top so Streamlit content doesn't overlap with navbar */
            .block-container {
                padding-top: 80px !important;
            }
        </style>

        <div class="custom-navbar">
            <div class="left">ResumeGenius.ai</div>
            <div class="right">
                <a href="#">Services</a>
                <a href="#" class="register">Register</a>
                <a href="#" style="color:#2563EB; font-weight:600;">Login</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .full-width-banner {
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            margin-top: 2.5vw;
            margin-bottom: 0.5vw;
            width: 100vw;
            background: transparent;
            text-align: center;
            overflow-x: auto;
            white-space: nowrap;
            padding: 0px 0;
        }

        .full-width-banner p {
            color: black;
            font-size: 40px;
            font-weight: bold;
            font-family: "Segoe UI", sans-serif;
            margin: 0;
        }
        </style>

        <div class='full-width-banner'>
            <p>Your Next Job Starts with a Smarter Resume</p>
        </div>
    """, unsafe_allow_html=True)



    st.markdown("""
    <p style='text-align:center; 
        color:#2563EB;
        font-size:20px; 
        font-weight:bold;
        margin-top: 0vw; 
        font-family: "Segoe UI", sans-serif;
        margin-bottom: 3vw;'>
        Stand Out . Get Noticed . Get Hired   
    </p>
""", unsafe_allow_html=True)

    