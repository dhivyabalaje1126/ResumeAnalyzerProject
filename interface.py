#This file contains code and blocks for the app's interface
# This interface is deployed in Streamlit. Refer the README file for a link for the deployed webpage

import streamlit as st

# Import user-defined function from analysis.py file to analyze resume
from analysis import analyze_resume


st.title('Resume Analyzer 🪄📝֎🇦🇮')

st.text('This page application will help you to analyze your resume against a provided job description and gain useful insights for improvement')

st.sidebar.subheader('Please attach and upload your resume/CV here 📝')

pdf_doc = st.sidebar.file_uploader('Browse files..',type=['pdf'])

st.sidebar.text('Designed by Dhivya Balaje')
st.sidebar.text('My Linkedin: https://www.linkedin.com/in/dhivya-balaje-a4b886205/')
job_desc = st.text_area('Copy-paste the job description here',max_chars=20000)

submit = st.button('Generate results')
# This will run the generative model you've called in analysis.py
# Be careful, since these models are free and they have a limit to how many times it can be re-run
# If you get an error with the interface saying your model limit has exceeded, use another model


if submit:
    with st.spinner('Analyzing your resume...'):
        analyze_resume(pdf_doc,job_desc)


