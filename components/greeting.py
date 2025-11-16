import random

def greeting():
    try:
        response = random.choice([
            "Hello Sir! How can I assist you today?",
            "Hi Sir! What can I do for you?",
            "Good to see you, Sir. How can I help you?"
        ])
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
