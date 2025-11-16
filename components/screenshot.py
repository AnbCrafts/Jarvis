import subprocess
from PIL import ImageGrab
import datetime
import time
import os
import printGUI
from utils.speech import speak

def screenshot():
    answer = "Your screenshot will be taken in 5 second. Please arrange your screen."
    printGUI.gui_print(answer)
    speak(answer)
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(os.path.expanduser("~/Desktop/pythonScreenshot"), exist_ok=True)
        filepath = os.path.expanduser(f"~/Desktop/pythonScreenshot/screenshot_{timestamp}.png")
        time.sleep(10)
        img = ImageGrab.grab()
        img.save(filepath)
        subprocess.run(["osascript", "-e", 'beep'])
        
        if os.path.exists(filepath):
            print(f"Your path {filepath}")
            response =  "Screenshot saved successfully in python screenshot folder."
            return response
        else:
            response = "Screenshot failed or file not found."
            return response
    except PermissionError:
        response =  "Permission denied. Cannot create screenshot file."
        return response
    except Exception as e:
        response =  f"An unexpected error occurred: {e}"
        return response

def custom_screenshot():
    answer = "Please select the area you want to take screenshot."
    printGUI.gui_print(answer)
    speak(answer)
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        os.makedirs(os.path.expanduser("~/Desktop/pythonScreenshot"), exist_ok=True)
        filepath = os.path.expanduser(f"~/Desktop/pythonScreenshot/screenshot_{timestamp}.png")

        subprocess.run(["screencapture", "-i", filepath])

        if os.path.exists(filepath):
            print(f"Your path: {filepath}")
            response =  "Screenshot saved successfully in python screenshot folder."
            return response
        else:
            response =  "Screenshot failed or file not found."
            return response
    
    except subprocess.CalledProcessError as e:
        response =  f"Screenshot command failed: {e}"
        return response
    except PermissionError:
        reponse =  "Permission denied. Cannot create screenshot file."
        return response
    except Exception as e:
        response =  f"An unexpected error occurred: {e}"
        return response
