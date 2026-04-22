import os
import time
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, messages):
        for i in range(3):  # retry 3 times
            try:
                response = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                )
                return response.choices[0].message.content

            except Exception as e:
                logger.error(f"Error: {e}")
                time.sleep(2)

        return "AI not working"