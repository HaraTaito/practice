#slackbotライブラリ呼び出し
from slackbot.bot import respond_to
from slackbot.bot import listen_to

#おはようというコメントに”今日も頑張りましょう”を返す
#listen_toはメンションがなくても反応する
@listen_to('おはよう')
def greeting(message):
    message.reply('今日も頑張りましょう')
