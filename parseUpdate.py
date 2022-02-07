from spamCheck import *
from processQuery import *
from antiSpam import *
from isAdmin import *

parsed = []

last_message_date = [0]

sent_a_while_ago = []

last_spam_messageDate = [0]

def parseUpdate(update) :

    update_id = update["update_id"]

    if update_id not in parsed :

        parsed.insert(0,update_id)

        if "message" in update :

            message = update["message"]

            if  "entities" in message   :

                entities = message["entities"]

                entities_object = entities[0]

                entities_type = entities_object["type"]

                if entities_type == "bot_command" :

                    message_text = message["text"]

                    message_date = message["date"]

                    message_id = message["message_id"]

                    message_date = message["date"]

                    reply_to_message_id = None

                    chat = message["chat"]

                    chat_type = chat["type"]

                    chat_id = chat["id"]

                    if "title" in chat :

                        chat_title = chat["title"]

                if "sender_chat" in message :

                    sender_chat = message["sender_chat"]

                    sender_chat_id = sender_chat["id"]

                    sender_chat_type = sender_chat["type"]

                reply_to_chat_id = None

                reply_to_user_id = None

                if "reply_to_message" in message :

                    reply_to_message = message["reply_to_message"]

                    reply_to_message_id = reply_to_message["message_id"]

                    if "from" in reply_to_message :

                        from_user = reply_to_message["from"]

                        reply_to_user_id = from_user["id"]

                    if "chat" in reply_to_message :

                        reply_to_chat = reply_to_message["chat"]

                        reply_to_chat_id = reply_to_chat["id"]

                user = message["from"]

                user_id = user["id"]

                first_name = user["first_name"]

                result = 0

                admin = isAdmin(chat_id , user_id)

                if (chat_type == "group" or chat_type == "supergroup" ) and admin == 0    :

                    result = spamCheck(chat_id ,  message_text , message_id , message_date , user_id)

                if result == 0 :

                    processQuery(chat_id ,  message_text , message_id , first_name , reply_to_message_id , chat_type , user_id , reply_to_user_id )

                return "OK"
