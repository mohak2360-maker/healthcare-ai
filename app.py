import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Health Insights", page_icon="🩺", layout="centered")

st.title("🩺 AI Health Insights")
st.markdown("Upload your blood report, X-ray or any medical document")

uploaded_file = st.file_uploader("Choose PDF or Image", type= )

if uploaded_file:
    with st.spinner("Analyzing your report..."):
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            text = "".join(page.extract_text() for page in reader.pages)
            prompt = f"Analyze this medical report in simple language:\n\n{text}"
        else:
            prompt = "Analyze this medical image and explain the findings simply."
        
        response = model.generate_content(prompt)
        result = response.text
    
    st.success("✅ Analysis Complete!")
    st.subheader("📋 Analysis Result")
    st.write(result)
    
    st.warning("⚠️ This is AI generated analysis only. Please consult a real doctor.")

    st.download_button("Download Report", result, "health_report.txt")