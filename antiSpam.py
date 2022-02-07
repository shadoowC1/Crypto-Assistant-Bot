from sendMessage import *
from isAdmin import *
from deleteMessage import *


def antiSpam(chat_id, message_id , user_id , message_date ) :

    difference = message_date - last_spam_messageDate[0]

    isAdmin = isAdmin(chat_id , user_id)

    if  difference < 10800 and isAdmin == 0   :

        deleteMessage(chat_id , message_id)

    elif isAdmin == 0 :

        message = "Sorry , in order to not spam this group please do not send the same command multiple times . \n try again later ."

        sendMessage(chat_id , message_id , message)

        last_spam_messageDate.insert(0 , message_date)

    return "OK"
