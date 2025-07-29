import os
import streamlit as st 
import google.generativeai as genai

# Importing the user-defined extractPDF function from the file pdf.py
# This is an example of creating a modular application
from pdf import extractPDF

from dotenv import load_dotenv
load_dotenv()

#Accessing Google API key from the .env file
# Recommended to create any API key and store it in a .env file to access like this
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

# Calling genai model
model = genai.GenerativeModel('gemini-1.5-flash')
# To use other models, explore Google open gamma models and use the models listed there
# Be careful, since these models are free and they have a limit to how many times it can be re-run
# If you get an error with the interface saying your model limit has exceeded, use another model

# Creating a user-defined function to analyze pdf and job description
def analyze_resume(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf_text = extractPDF(pdf_doc) #extractPDF() from pdf.py called here
        st.write('Resume information read successfully 🪄')
    else:
        st.warning('Drop a file in PDF format')
    
    model_answer = model.generate_content(f'''
                           You will first analyze the resume {pdf_text}.
                           Compare the resume {pdf_text} with the given job description {job_desc}
                           and analyze how fit this candidate is for the given job. Score the resume out of 100 based on how
                           fit it is with the description of the job.
                           Display the candidate's strengths, weaknesses, and ways they can improve their resume
                           to newer levels. Also, list out some job positions they may be well-qualified for.
                           Also, provide a list of possible courses or activities they can undertake to develop their skills further.
                           Finally, provide an overall assessment -- a summary of sorts that's short.
                           Don't be too wordy. Use concise, clear bullet points that's easy to read and understand.''')
    
    return st.write(f'{model_answer.text}')



