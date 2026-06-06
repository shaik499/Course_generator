from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_course(topic, level, duration, audience):

    prompt = f"""
    Create a complete course.

    Topic: {topic}
    Level: {level}
    Duration: {duration}
    Audience: {audience}

    Include:
    1. Course Title
    2. Course Description
    3. Learning Outcomes
    4. Weekly Modules
    5. Quiz Questions
    6. Assignment Ideas
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content