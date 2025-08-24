import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose a Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Test prompt
response = model.generate_content("Hello Gemini! Tell me why AI is exciting in 2 lines.")
print(response.text)
