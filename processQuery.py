from getReplyMarkupCommand import *
from getReplyMarkup import *
from getReply import *
from sendReplyMarkup import *
from getDataCommand import *
from getFeyData import *
from getDataReply import *
from sendMessage import *
from getModerationCommand import *
from deleteMessage  import *
from isAdmin import *
from ban import *

def processQuery(chat_id , message_text , message_id , first_name , reply_to_message_id , chat_type , user_id , reply_to_user_id ) :

    command = message_text

    replyMarkup_command = getReplyMarkupCommand(command)

    if replyMarkup_command != 0 :

        replyMarkup = getReplyMarkup(replyMarkup_command)

        reply_text = getReply(replyMarkup_command)

        sendReplyMarkup(chat_id , message_id , replyMarkup , reply_text)

        return 1

    data_command = getDataCommand(command)

    if data_command != 0 :

        dataResult = getFeyData(data_command)

        reply = getDataReply(data_command)

        message = str(reply) + str(dataResult)

        sendMessage(chat_id , message_id , message )

        return 1

    ModerationCommand = getModerationCommand(command)

    if ModerationCommand != 0 and (chat_type == "group" or chat_type == "supergroup") and reply_to_message_id != None :

            if isAdmin(chat_id , user_id) == 1 or user_id ==  :

                if ModerationCommand == "/delete" :

                    message = "op op "
                    botMessage_id = sendMessage(chat_id , message_id , message)
                    deleteMessage(chat_id , reply_to_message_id)
                    deleteMessage(chat_id , message_id)
                    deleteMessage(chat_id , botMessage_id)

                    return 1

                if ModerationCommand == "/ban" :
                    message = "op op "
                    botMessage_id = sendMessage(chat_id , message_id , message)
                    ban(chat_id, reply_to_user_id)
                    deleteMessage(chat_id , message_id)
                    deleteMessage(chat_id , botMessage_id)

                    return 1

            else :

                deleteMessage(chat_id , message_id)

                return 0

    if command == "/start" and chat_type  == "private" :

        message = "Welcome " + first_name + " , Please chose from the list of commands to get Started !"

        sendMessage(chat_id , message_id , message)

        return 1


    else :

        message = "Unrecognized command. Say what?"

        sendMessage(chat_id , message_id , message)

        return 0
