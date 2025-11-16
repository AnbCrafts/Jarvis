from utils.speech import speak
import printGUI

def introduce_friday():
    intro_lines = [
        "Hello Sir",
        "I am FRIDAY a Female Replacement Intelligent Digital Assistant Youth.",
        "I’m your personal AI assistant, designed to help you manage tasks, answer questions, and make your digital life easier.",
        "I can take notes, tell time, take screenshots, send whatsApp, open websites and even talk with you naturally.",
    ]

    # Speak each line naturally
    for line in intro_lines:
        printGUI.gui_print(f"FRIDAY: {line}")
        speak(line, blocking=True)

    response = "Always here to assist you, Sir!"
    return response
