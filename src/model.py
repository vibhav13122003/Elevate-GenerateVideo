import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI


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

    @staticmethod
    def openai_chatgpt(transcript, prompt, extra=""):
        client = OpenAI(api_key=os.getenv("OPENAI_CHATGPT_API_KEY"))
        try:
            response = client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt + extra + transcript}]
            )
            return response.choices[0].message["content"]
        except Exception as e:
            return f"⚠️ API Error: {e}"
