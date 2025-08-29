from groq import Groq
from dotenv import load_dotenv
import os

import config


load_dotenv(config.dirPath + "/groq_api.env")

client = Groq(api_key=os.getenv("groq_API_KEY"))

def ask_gpt(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Ты — помощник."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
