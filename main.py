import vk, time, random

session = vk.AuthSession(access_token='')
api = vk.API(session)
chatid = input('Enter id: ')
chatname = input('Enter name: ')
mess = input('Enter message: ')
print(' ')
while True:
    chat = api.messages.getChat(chat_id=chatid)
    if chat['title'] == chatname:
        print('{} ...[OK]'.format(chatname))
    else:
        print("{} ...[ERROR]".format(chatname))
        r = random.randint(1, 100000)
        api.messages.send(chat_id=chatid, message=mess, guid=r)
        api.messages.editChat(chat_id=chatid, title=chatname)
    time.sleep(1)
