import os
from dotenv import load_dotenv
import google.generativeai as genai



class Model:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def google_gemini(transcript, prompt, extra=""):
        # Configure the Gemini API
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        print("Configuration successful!")
        model = genai.GenerativeModel("gemini-pro")
        try:
            # Generate text using the Gemini API
           
            response = model.generate_content(prompt + extra + transcript)
            return response.text
        except Exception as e:
            return f"⚠️ API Error: {e}"

