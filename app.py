import streamlit as st
from utils.analyzer import analyze_report

st.set_page_config(page_title="AI Health Insights", page_icon="🩺", layout="wide")

st.title("🩺 AI Health Insights")
st.write("Upload your blood report, X-ray or any medical document")

uploaded_file = st.file_uploader("Choose PDF or Image file", type= )

if uploaded_file:
    with st.spinner("Analyzing your report..."):
        result = analyze_report(uploaded_file)
    
    st.success("✅ Analysis Complete!")
    st.subheader("AI Analysis Result:")
    st.write(result)
    
    st.warning("⚠️ This is AI-generated analysis only. Please consult a real doctor.")