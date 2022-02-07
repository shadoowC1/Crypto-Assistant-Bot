import requests
import json

def sendMessage(chat_id , message_id , message) :

    send_message =  "https://api.telegram.org/bot<token>/sendMessage"

    message = {"chat_id":chat_id , "text":message , "reply_to_message_id":message_id}

    response = requests.post(send_message , message)

    update = response.json()

    if "result" in update :

        result = update["result"]

        botMessage_id = result["message_id"]

        return botMessage_id
    else :

        return 0
