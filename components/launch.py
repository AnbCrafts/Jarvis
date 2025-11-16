import pyautogui
import time

def launch(request):
    try:
        query = request.replace("launch", "").strip()
        pyautogui.hotkey("command", "space")
        time.sleep(1.5)
        pyautogui.write(query)
        time.sleep(0.5)
        pyautogui.press("enter")
        response = f"Launching {query}"
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
