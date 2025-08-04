import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_supplier_risk(comment):
    prompt = (
        f"Read the following supplier comment and rate the risk from 1 (low) to 10 (high):\n\n"
        f"Comment: {comment}\nJust return the number."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"].strip()
