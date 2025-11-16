from utils.speech import speak, listen_once
import printGUI
import datetime
import pywhatkit as pwk

def whatsApp():
    try:
        contact_Que = "Who do you want to message?"
        printGUI.gui_print(contact_Que)
        speak(contact_Que, blocking=True)

        contact_Ans = listen_once()
        contact_Ans = contact_Ans.lower().strip()

        contactList = {
            "aakash": "+916290997831",
            "suraj": "+917044706644",
            "mom": "+911234567890"
        }

        if contact_Ans in contactList:
            number = contactList[contact_Ans]
        elif contact_Ans == "":
            response = "Try again after sometime"
            
            return response
        
        else:
            response = "Sorry, I don’t have that contact saved."
            
            return response
        
        message_Que = "What do you want to message?"
        printGUI.gui_print(message_Que)
        speak(message_Que, blocking=True)

        message_Ans = listen_once()

        printGUI.gui_print(f"I’m preparing your message --{message_Ans}-- to send to --{contact_Ans}-- ")
        speak(f"I’m preparing your message --{message_Ans}-- to send to --{contact_Ans}-- ", blocking=True)
        
        pwk.sendwhatmsg_instantly(number, message_Ans, wait_time=20, tab_close=True)

        response = "Message send successfully, sir."
        return response

    except Exception as e:
        
        printGUI.gui_print(f"Sorry, I couldn't send the WhatsApp message.", e)
        response  = "Sorry, I couldn't send the WhatsApp message."
        return response
    
def whatsApp_text(query):
    try:
        # Remove the word 'send' from start
        query = query.replace("send", "", 1).strip()

        # Split into message and number at the first occurrence of 'to'
        parts = query.split("to", 1)
        if len(parts[0]) < 1:
            response =  "Write some" \
            "thing, your message is empty."
        else:
            message = parts[0].strip().strip("'\"")   # remove extra quotes if any
            number = parts[1].strip()

            # Handle short or invalid numbers
            if not number.isdigit():
                response = "Write in this pattern = send YOUR MESSAGE to PHONE NUMBER"
                
            else:
                if len(number) == 10:
                    phone = "+91" + number
                    printGUI.gui_print(f"Sending --{message}-- to --{phone}-- ")
                    speak(f"Sending --{message}-- to --{phone}-- ", blocking=True)
                    pwk.sendwhatmsg_instantly(phone, message, wait_time=20, tab_close=True)
                    response = "Message send successfully sir."
                else:
                    response = "Invalid phone number."
    except Exception as e:
        print("Error:", e)
        response = "Something went wrong while sending your message."
    return response


