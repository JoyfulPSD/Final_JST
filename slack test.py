import time
import pyupbit
import datetime
import requests
import schedule
import slacker

myToken = 'xoxb-3369599391971-3393361783648-BxkgtZZ4kfsVW2lUkHFyUX85'


def post_message(token, channel, text):
    #"""슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def job():
    post_message(myToken,"#jst-coin", "autotrade start")


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
