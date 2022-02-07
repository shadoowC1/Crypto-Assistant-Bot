
def spamCheck(chat_id ,  message_text , message_id , message_date , user_id) :

    messages_time_difference =  message_date - last_message_date[0]

    if messages_time_difference > 2500 or message_text not in sent_a_while_ago :

        sent_a_while_ago.append(message_text)

        if len(sent_a_while_ago) == 4 :

            sent_a_while_ago.clear()

        last_message_date.insert(0,message_date)

        return 0

    else :

        antiSpam(chat_id , message_id , user_id , message_date)
        return 1
