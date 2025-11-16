---

# 🧠 **Jarvis – AI Voice Assistant (Python)**

A powerful desktop voice assistant built with Python that can speak, listen, process user commands, automate tasks, and integrate with AI APIs like OpenAI.

---

## 🚀 **Features**

* 🎤 **Voice Recognition** (speech-to-text)
* 🔊 **AI-generated responses** using OpenAI
* 📧 **Email Automation** (Sendinblue SMTP / SMTP APIs)
* 🔍 **Web Search & Browsing**
* 📁 **File operations** (open apps, create notes, etc.)
* 🕰️ **System tasks** (time, date, battery info, shutdown commands)
* 📢 **Text-to-speech (TTS)**
* ⚡ **Hotword Activation** (Jarvis wake word)
* 🛡️ **Secure environment-based API key handling**
* 🧩 Modular, scalable codebase

---

## 🛠️ **Tech Stack**

| Component        | Technology                    |
| ---------------- | ----------------------------- |
| Language         | Python                        |
| STT              | SpeechRecognition             |
| TTS              | pyttsx3                       |
| AI Model         | OpenAI API                    |
| Emails           | Sendinblue SMTP API           |
| Environment Vars | python-dotenv                 |
| Others           | requests, webbrowser, smtplib |

---

## 📂 **Project Structure**

```
Jarvis/
│
├── core/
│   ├── speech_engine.py
│   ├── listener.py
│   ├── ai_handler.py
│   └── command_router.py
│
├── utils/
│   ├── email_service.py
│   ├── system_tasks.py
│   └── config_loader.py
│
├── main.py
├── README.md
├── .env
└── requirements.txt
```

---

## 🔧 **Setup Instructions**

### **1️⃣ Clone the Repository**

```
git clone https://github.com/AnbCrafts/Jarvis.git
cd Jarvis
```

### **2️⃣ Create & Activate Virtual Env**

```
python -m venv venv
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**

```
pip install -r requirements.txt
```

### **4️⃣ Create `.env` File (IMPORTANT)**

Create a `.env` file in root:

```
OPENAI_API_KEY=your_key_here
SMTP_KEY=your_smtp_key_here
SENDER_EMAIL=your_email
RECEIVER_EMAIL=default_receiver
```

### **5️⃣ Run Jarvis**

```
python main.py
```

---

## 🔐 **Security Notice**

This project uses **environment variables** to protect sensitive API keys.
DO NOT store API keys inside source code.

---

## 📬 **Available Voice Commands**

* “Jarvis, search for ___”
* “Send an email to ___”
* “What is the time/date?”
* “Open YouTube / Notepad / etc.”
* “Write a note”
* “Tell me about ___”
* “Shut down / restart the system”

---

## 👨‍💻 **Contributing**

Pull requests are welcome!
If you have suggestions for improvements, feel free to open an issue.

---

## 📜 **License**

This project is licensed under the **MIT License**.

---

## ⭐ **Show Your Support**

If you like this project:

**Give it a ⭐ on GitHub!** 🙌



