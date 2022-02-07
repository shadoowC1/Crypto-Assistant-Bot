import requests 

def sendReplyMarkup(chat_id , message_id , replyMarkup , reply_text) :

    send_message =  "https://api.telegram.org/bot<token>/sendMessage"

    message = {"chat_id":chat_id , "text":reply_text , "reply_markup":replyMarkup , "reply_to_message_id":message_id}

    requests.post(send_message , message)
