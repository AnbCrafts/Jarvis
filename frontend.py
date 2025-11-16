import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from main import main_process, speak, command, process_command
from utils.speech import listen_once
from printGUI import set_gui_callback

class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS AI Assistant")
        self.root.geometry("600x400")
        self.root.config(bg="#101820")

        self.title = tk.Label(root, text="JARVIS AI Assistant", font=("Arial", 18, "bold"), fg="#00FFFF", bg="#101820")
        self.title.pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, bg="#0D1B2A", fg="#00FFEF", font=("Consolas", 11))
        self.output.pack(pady=10)

        self.entry = tk.Entry(root, width=60, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, padx=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_command, bg="#00FFFF", fg="black")
        self.send_button.pack(side=tk.LEFT)

        self.voice_button = tk.Button(root, text="🎙 Speak", command=self.voice_command, bg="#00FFEF", fg="black")
        self.voice_button.pack(side=tk.LEFT)

    def send_command(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.output.insert(tk.END, f"You: {text}\n")
        Thread(target=self.handle_command, args=(text,)).start()

    def voice_command(self):
        self.output.insert(tk.END, "🎤 Listening...\n")
        Thread(target=self.listen_and_handle).start()

    def listen_and_handle(self):
        text = command()
        self.output.insert(tk.END, f"You said: {text}\n")
        self.handle_command(text)
        self.output.see(tk.END)

    def handle_command(self, text):
        response = process_command(text)
        self.output.insert(tk.END, f"JARVIS: {response}\n")
        self.output.see(tk.END)

    def show_message(self, text):
        self.output.insert(tk.END, f"JARVIS: {text}\n")
        self.output.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    set_gui_callback(app.show_message)  # Connect GUI to backend
    app.show_message("JARVIS activated. Awaiting your command, Sir.")
    speak("JARVIS activated. Awaiting your command, Sir.")
    root.mainloop()
