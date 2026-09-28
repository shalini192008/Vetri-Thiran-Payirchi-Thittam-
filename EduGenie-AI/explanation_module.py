import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def explain_topic(topic: str):

    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic clearly and accurately:

{topic}

Use simple language suitable for college students.

Include:
1. Definition
2. Main points
3. Simple example
4. Real-world application
5. Short conclusion

Make the explanation easy to understand and remember.
"""

    try:

        response = client.models.generate_content(
           model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"