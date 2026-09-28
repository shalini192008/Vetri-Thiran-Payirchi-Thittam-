import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_quiz(topic: str):

    prompt = f"""
You are EduGenie, an educational AI assistant.

Create exactly 3 multiple-choice questions about:

{topic}

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question here",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A"
  }}
]

Do not add markdown or explanations outside JSON.
"""

    try:

        response = client.models.generate_content(
          model="gemini-3.5-flash-lite",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e)
        }