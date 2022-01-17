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
    url2 = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat}&text={msg}&parse_mode=html'.replace("&amp;",'')
    return url2

def send_up(updates,chats):
    for msg in updates:
        for chat in chats:
            # url = get_url(msg,chat)
            # print(url)
            res = requests.request("GET",get_url(msg,chat))

def main():
    chats=set()
    last=1
    c=0
    while True:
        if c==0:
            res = requests.request("GET",url1).json()
            for ch in res['result']:
                print("Adding chat ids")
                try:chats.add(ch['message']['chat']['id'])
                except:continue
        print(chats)
        print("Chat List Fetched")
        latest,updates=tweet.main()
        print('Tweets Fetched')
        # print(updates)
        if latest!=last:
            print(latest,last)
            last=latest
            send_up(updates,chats)
            time.sleep(5)
        c = 0 if c==100 else c+1
        time.sleep(20)

if __name__ == "__main__":
    main()
