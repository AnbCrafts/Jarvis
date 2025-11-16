import os
import printGUI
from pync import Notifier
from utils.speech import speak

def add_new_task(request):
    try:
        task = request.lower().split("new task", 1)[-1].strip()

        if task:
            todo_file = os.path.expanduser("~/Desktop/pythonScreenshot/todo.txt")
            os.makedirs(os.path.dirname(todo_file), exist_ok=True)

            with open(todo_file, "a") as file:
                file.write(task + "\n")

            response = f"Task added successfully: {task}"
        else:
            response = "No task found to add. Please say something after 'new task'."
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response



def delete_all_tasks():
    try:
        todo_file = os.path.expanduser("~/Desktop/pythonScreenshot/todo.txt")

        if not os.path.exists(todo_file):
            response = "No task file found yet."
            return response

        with open(todo_file, "w") as file:
            file.truncate(0)

        response = "All tasks have been deleted successfully."
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response



def delete_specific_task(request):
    try:
        todo_file = os.path.expanduser("~/Desktop/pythonScreenshot/todo.txt")

        if not os.path.exists(todo_file):
            response = "No task file found yet."
            return response

        task_to_delete = request.replace("delete", "").replace("task", "").strip().lower()

        with open(todo_file, "r") as file:
            tasks = file.readlines()

        if not tasks:
            response = "Your to-do list is empty."
            return response

        remaining_tasks = [t for t in tasks if task_to_delete not in t.lower()]

        if len(remaining_tasks) == len(tasks):
            response = f"Task '{task_to_delete}' not found in your list."
        else:
            with open(todo_file, "w") as file:
                file.writelines(remaining_tasks)
            response = f"Task '{task_to_delete}' deleted successfully."

    except Exception as e:
        response = f"An unexpected error occurred: {e}"

    return response



def speak_all_tasks():
    try:
        todo_file = os.path.expanduser("~/Desktop/pythonScreenshot/todo.txt")

        if not os.path.exists(todo_file):
            response = "You don't have any task file yet."
            return response

        with open(todo_file, "r") as file:
            tasks = [t.strip() for t in file.readlines() if t.strip()]

        if not tasks:
            response = "Your to-do list is empty."
            return response
        
        heading = "Here are your current tasks:"
        printGUI.gui_print(heading)
        speak(heading, blocking=True)

        for i, task in enumerate(tasks, start=1):
            answer = f"Task {i}: {task}"
            printGUI.gui_print(answer)
            speak(answer, blocking=True)

        response = "All tasks have been read successfully."
        return response
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
        return response



def show_all_tasks():
    try:
        todo_file = os.path.expanduser("~/Desktop/pythonScreenshot/todo.txt")

        if not os.path.exists(todo_file):
            response = "You don't have any task file yet."
            Notifier.notify(title="Today's Work", message=response, sound="default")
            return response
        else:
            with open(todo_file, "r") as file:
                tasks = [t.strip() for t in file.readlines() if t.strip()]

            if not tasks:
                response = "Your to-do list is empty."
                Notifier.notify(title="Today's Work", message=response, sound="default")
                return response
            else:
                formatted_tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
                Notifier.notify(title="Today's Work", message=formatted_tasks, sound="default")
                
                response = "Your task notification send successfully."
                return response
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
        return response




