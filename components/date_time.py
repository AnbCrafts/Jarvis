import datetime

def dates():
    try:
        now_date = datetime.datetime.now().strftime("%d/%m/%Y")
        response = f"Current date is {now_date}"
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response

def times():
    try:
        now_time = datetime.datetime.now().strftime("%H:%M")
        response = f"Current time is {now_time}"
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
