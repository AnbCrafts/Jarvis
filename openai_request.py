
import os
import user_config
from google import genai

try:
    client = genai.Client(api_key=user_config.gemini_key)
except Exception as e:
    print(f"Error initializing client: {e}")
# prompt = "Write a one-paragraph bedtime story about a unicorn."

def send_request(query):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query
        )

        # 3. Print the output
        return response.text

    except Exception as e:
        return (f"An error occurred during model generation: {e}")
    

    # def send_request(query):
    # try:
    #     speech_prompt = (
    #         "You are JARVIS, an AI voice assistant. "
    #         "Respond to the following user query in a friendly, natural, and speech-optimized way. "
    #         "Use short sentences and simple language so it sounds great when spoken aloud. "
    #         "Avoid long paragraphs and complex punctuation.\n\n"
    #         f"User: {query}\n"
    #         "JARVIS:"
    #     )

    #     response = client.models.generate_content(
    #         model="gemini-2.5-flash",
    #         contents=speech_prompt
    #     )

    #     return response.text.strip()

    # except Exception as e:
    #     return f"An error occurred during model generation: {e}"
