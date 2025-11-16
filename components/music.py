import webbrowser
import random

def music():
    try:
        response = "Playing music..."
        song = random.choice([
            "https://youtu.be/W6Op1RjLXQg",
            "https://youtu.be/Abk7L9zmbG4",
            "https://youtu.be/M8nhouDBIjY"
        ])
        webbrowser.open(song)
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
