from whatsapp2 import WhatsApp
whatsapp = WhatsApp(100, session="mysession")
user_names = whatsapp.unread_usernames(scrolls=100)
for name in user_names:
    messages = whatsapp.get_last_message_for(name)
    messgaes_len = len(messages)
    latest_msg = messages[messgaes_len-1]