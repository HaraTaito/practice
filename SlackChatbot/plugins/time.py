from slackbot.bot import respond_to
from slackbot.bot import listen_to

import datetime
import time

@listen_to('今何時？')
def res_time(message):
    dt_now=datetime.datetime.now()
    #現在時刻の返信
    time_str=dt_now.strftime('%H時%M分です。')
    message.send(time_str)

    #時間帯別にコメントを変える
    if dt_now.hour ==11:
        res='お昼までもう少しです'
    elif dt_now==15:
        res='おやつですよーーーーそうなのーーー'
    else:
        res='昨日の自分を超えて行け'
    #1mディレイ
    time.sleep(1)
    #1言コメント送信
    message.send(res)
    
