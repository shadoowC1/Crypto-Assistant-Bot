import requests

def deleteMessage(chat_id ,message_id) :

    delete_message =  "https://api.telegram.org/bo<token>/deleteMessage"

    data = {"chat_id":chat_id , "message_id":message_id}

    response = requests.post(delete_message , data)

    update = response.json()

    ok = update["ok"]

    return ok
