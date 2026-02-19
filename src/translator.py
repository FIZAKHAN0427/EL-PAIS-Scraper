import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

HEADERS = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}


def translate_to_english(spanish_text):

    if not spanish_text:
        return ""

    payload = {
        "from": "es",
        "to": "en",
        "q": [spanish_text]
    }

    try:

        response = requests.post(
            URL,
            json=payload,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            return result[0]

        return spanish_text

    except Exception as e:

        print("Translation failed:", e)

        return spanish_text