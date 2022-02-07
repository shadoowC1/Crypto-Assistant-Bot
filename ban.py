import requests

def ban(chat_id, reply_to_user_id)  :

    endPoint = "https://api.telegram.org/bot<token>/banChatMember"

    data = {"chat_id":chat_id , "user_id":reply_to_user_id}

    requests.post(endPoint , data)

    return "OK"
