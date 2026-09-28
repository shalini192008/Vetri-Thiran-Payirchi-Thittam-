import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def summarize_text(text: str):

    prompt = f"""
Summarize the following educational content.

Requirements:
- Keep the important points
- Use simple language
- Use bullet points where useful
- Do not remove important information

Content:
{text}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"