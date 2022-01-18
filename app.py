import requests
import time
import json
import os
import tweet

bot_token = os.environ['tkey']
url1 = "https://api.telegram.org/bot{}/getUpdates".format(bot_token)

def get_url(msg,chat):
    if(len(msg)>1):msg = "<b>RONB Update</b> \n\n"+msg
    # print(112,msg)
    url2 = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat}&text={msg}&parse_mode=html'.replace("&amp;",'%26').replace("#","%23").replace("https://t.co","\nhttps://t.co")
    return url2

def send_up(last,updates,chats):
    for msg in updates:
        for chat in chats:
            url = get_url(msg['text'],chat)
            print("next")
            if msg['id']==last:return True
            res = requests.request("GET",get_url(msg['text'],chat))
    return True

def main():
    chats=set()
    last=1483318011402461190
    c=0
    while True:
        if c==0:
            res = requests.request("GET",url1).json()
            for ch in res['result']:
                try:
                    if 'message' in ch.keys():chats.add(ch['message']['chat']['id'])
                    if 'channel_post' in ch.keys():chats.add(ch['channel_post']['chat']['id'])
                except:continue

        # print(chats)
        print("Chat List Fetched")
        latest,updates=tweet.main()
        print('Tweets Fetched')
        # print(updates)
        if latest!=last:
            print(latest,last)
            send_up(last,updates,chats)
            last=latest
            time.sleep(5)
        c = 0 if c==100 else c+1
        time.sleep(20)

if __name__ == "__main__":
    main()
