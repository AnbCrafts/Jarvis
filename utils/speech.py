import playsound
import tempfile
import time
import os
import threading
from gtts import gTTS
import speech_recognition as sr
import printGUI

def speak(command, blocking=False):
    cleaned_command = command.replace('**', ' ').strip()
    if not cleaned_command:
        return

    def _speak():
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts = gTTS(text=cleaned_command, lang='hi')
                tts.save(fp.name)
                playsound.playsound(fp.name, block=True)  # Waits until done
            os.remove(fp.name)
        except Exception as e:
            print("Speech error:", e)
            printGUI.gui_print("Speech error:", e)

    if blocking:
        _speak()  # Speak and wait until finished
    else:
        threading.Thread(target=_speak, daemon=True).start()  # Background speech




def confirm_text(text):
    question = "Was that right? 'yes confirmed' or 'not correct'."
    printGUI.gui_print(question)
    speak(question, blocking=True)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        printGUI.gui_print("🎤 Listening confirmation...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            confirmation = r.recognize_google(audio, language='en-in').lower()
            printGUI.gui_print(f"You said: {confirmation}")

            if "yes" in confirmation:
                answer = "✅Confirmed."
                printGUI.gui_print(answer)
                speak(answer, blocking=True)
                
                return text
            
            elif "not" in confirmation:
                answer = "Okay, please say it again."
                printGUI.gui_print(answer)
                speak(answer, blocking=True)

                return listen_once()
            
            else:
                answer = "⚠️ Didn't catch that. Please respond with 'yes confirmed' or 'not correct'."
                printGUI.gui_print(answer)
                speak(answer, blocking=True)

                return confirm_text(text)
            
        except sr.UnknownValueError:
            answer = "I didn't catch that, please respond with 'yes confirmed' or 'not correct'."
            printGUI.gui_print(answer)
            speak(answer, blocking=True)

            return confirm_text(text)
        
        except sr.WaitTimeoutError:
            answer = "No response detected, please confirm again."
            printGUI.gui_print(answer)
            speak(answer, blocking=True)

            return confirm_text(text)
        
        except sr.RequestError:
            answer = "Network error while confirming."
            printGUI.gui_print(answer)
            speak(answer, blocking=True)

            return ""



def listen_once():
    """Listen for voice input and confirm before returning."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        printGUI.gui_print("🎤 Listening...")
        audio = r.listen(source, timeout=None, phrase_time_limit=10)

    try:
        text = r.recognize_google(audio, language='en-in').strip()
        
        answer = f"You said: {text}"
        printGUI.gui_print(answer)
        speak(answer, blocking=True)

        response = confirm_text(text)
        return response

    except sr.UnknownValueError:
        answer = "Could not understand. Try again."
        printGUI.gui_print(answer)
        speak(answer, blocking=True)

        return listen_once()
    
    except sr.RequestError:
        answer = "Network error: could not connect to speech service."
        printGUI.gui_print(answer)
        speak(answer, blocking=True)

        return ""

    
    
