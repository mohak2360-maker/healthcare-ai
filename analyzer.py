import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment (Render uses this)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API Key not found!")
    st.stop()

genai.configure(api_key=api_key)

def analyze_report(uploaded_file):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if uploaded_file.type == "application/pdf":
            from PyPDF2 import PdfReader
            reader = PdfReader(uploaded_file)
            text = "".join(page.extract_text() for page in reader.pages)
            prompt = f"Analyze this medical report in simple and clear language:\n\n{text}"
        else:
            prompt = "Analyze this medical image/report and explain the findings in simple language."
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error analyzing report: {str(e)}\n\nPlease check your Gemini API key."