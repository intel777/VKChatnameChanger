import vk
import time

session = vk.AuthSession(access_token='')
api = vk.API(session)

chatid = 
chatname =

while True:
    chat = api.messages.getChat(chat_id=chatid)
    if chat['title'] == chatname:
        print('С беседой все впорядке')
    else:
        print('Changes detected!)
        api.messages.editChat(chat_id=chatid, title=chatname)
    time.slep(1)
