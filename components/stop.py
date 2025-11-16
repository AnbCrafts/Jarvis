import printGUI
import os
from utils.speech import speak
def stop():
    response = "Goodbye sir, have a nice day!"
    printGUI.gui_print(response)
    speak(response, blocking=True)
    os._exit(0)
    return
