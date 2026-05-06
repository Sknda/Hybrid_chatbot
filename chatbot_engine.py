import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def load_rules():
    """Loads the predefined rules from the JSON file."""
    try:
        with open("rules.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"keywords": {}}

def get_response(user_input, chat_history):
    """
    Triage Logic:
    1. Check for Exact Rule Match.
    2. If no match, call LLM with History.
    """
    rules = load_rules()
    user_input_clean = user_input.lower().strip()

    # --- Step 1: Exact Rule Match ---
    if user_input_clean in rules["keywords"]:
        return rules["keywords"][user_input_clean], True  # True means it's a rule

    # --- Step 2: Generative Fallback ---
    try:
        # Convert Streamlit history format to Gemini format
        formatted_history = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            formatted_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=formatted_history)
        response = chat.send_message(user_input)
        return response.text, False
    except Exception as e:
        return f"Error connecting to AI: {str(e)}", False