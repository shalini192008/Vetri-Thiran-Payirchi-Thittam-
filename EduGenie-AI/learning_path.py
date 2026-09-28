import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def get_learning_recommendations(topic: str):

    prompt = f"""
You are EduGenie, an educational AI assistant.

Create a personalized learning path for:

{topic}

Organize it into:

1. Beginner level
2. Intermediate level
3. Advanced level

For each level provide:
- Topics to learn
- Short explanation
- Practice activities
- Useful resource suggestions

Make the plan easy for a college student to follow.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"