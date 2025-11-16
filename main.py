# import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import pyautogui
import time
import wikipedia
import pywhatkit as pwk
import smtplib
import sys
from gtts import gTTS
import playsound
import tempfile
import os
import threading
from email.mime.text import MIMEText
from pync import Notifier
import user_config
import printGUI
import openai_request as ai
from utils.speech import speak, listen_once
from components.stop import stop
from components.introduction import introduce_friday
from components.search import search
from components.launch import launch
from components.music import music
from components.wikipedia import search_wikipedia
from components.date_time import dates, times
from components.greeting import greeting
from components.website import website
from components.screenshot import screenshot, custom_screenshot
from components.whatsapp import whatsApp, whatsApp_text
from components.email import send_email_via_brevo
from components.tasks import add_new_task, delete_all_tasks, delete_specific_task,speak_all_tasks, show_all_tasks

# from analytic import log_result, start_timer
# import uuid


def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            content = r.recognize_google(audio, language = 'en')
            print("You said....." + content)
        except Exception as e:
            print("Please try again...")
    
    return content

# def detect_category(query):
#     query = query.lower()
#     if any(word in query for word in ["time", "date"]):
#         return "datetime"
#     elif any(word in query for word in ["wikipedia", "google", "search"]):
#         return "search"
#     elif "music" in query:
#         return "entertainment"
#     elif "task" in query:
#         return "task_management"
#     elif "whatsapp" in query or "email" in query:
#         return "communication"
#     elif "ai" in query:
#         return "ai_query"
#     else:
#         return "general"

def process_command(request):
    request = request.lower().strip()
    response = ""

    # query_id = str(uuid.uuid4())
    # start_timer(query_id)

    try:
        if "hello" in request:
            response = greeting()

        elif "who are you" in request or "introduce yourself" in request or "your name" in request:
            response = introduce_friday()


        elif "time" in request:
            response = times()

        elif "date" in request:
            response = dates()

        elif "wikipedia" in request:
            response = search_wikipedia(request)

        elif "search on google" in request:
            response = search(request)

        elif "launch" in request:
            response = launch(request)

        elif "play music" in request:
            response = music()

        elif "website" in request:
            response = website(request)

        elif "custom screenshot" in request:
            response = custom_screenshot()

        elif "screenshot" in request:
            response = screenshot()

        elif "new task" in request:
            response = add_new_task(request)

        elif "speak all task" in request:
            response = speak_all_tasks()

        elif "show all task" in request:
            response = show_all_tasks()

        elif "delete all task" in request:
            response = delete_all_tasks()

        elif "delete" in request:
            response = delete_specific_task(request)

        elif "send whatsapp" in request:
            response = whatsApp()

        elif "send" in request and "to" in request:
            response = whatsApp_text(request)

        elif "send email" in request:
            success, response = send_email_via_brevo(
            to_email="aky21062002yadav@gmail.com",
            subject="Hello from your assistant FRIDAY",
            body="This is a test email.")
            print(success)

        elif "ask ai" in request:
            query = request.replace("ask ai", "").strip()
            ai_response = ai.send_request(query)
            response = ai_response

        elif "stop" in request or "exit" in request or "close" in request:
            response = stop()

        else:
            response = "I'm still learning that command!"

    # except KeyboardInterrupt:
    #     print("\nProgram interrupted by user. Shutting down.")
    #     response = "Goodbye sir, have a nice day!"

    except Exception as e:
        print("Error in processing command:", e)
        response = "Sorry, I ran into an issue."

    # log_result(query_id, request, detect_category(request), response)
    # Speak & return text
    speak(response)
    return response
def main_process():
    import speech_recognition as sr
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-in')
            print("You said:", text)
            response = process_command(text)
            print("Jarvis:", response)
        except:
            print("Could not understand, please try again.")
    