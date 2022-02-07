import requests
import json

def isAdmin(chat_id , user_id) :

    chat_admins = []

    chatAdmins_endPoint =  "https://api.telegram.org/bot<token>/getChatAdministrators"

    data = {"chat_id":chat_id}

    response = requests.get(chatAdmins_endPoint , data)

    update = response.json()

    if "result" in update :

        admins = update["result"]

        for i in range(0 , len(admins)) :

            admin = admins[i]

            user = admin["user"]

            admin_id = user["id"]

            chat_admins.append(admin_id)

    if user_id in chat_admins :

        return 1

    else :

        return 0
