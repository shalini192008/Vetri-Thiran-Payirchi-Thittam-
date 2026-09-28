from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def answer_question(question: str):

    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Use simple language suitable for college students.

Question:
{question}

Give a clear and easy-to-understand answer.
"""

    try:
        response = client.models.generate_content(
           model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"