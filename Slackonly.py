import time
import pyupbit
import datetime
import schedule
import requests
from fbprophet import Prophet

myToken = 'xoxb-3369599391971-3393361783648-IKu7bM51WerOcktzHTgxxN5A'

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

predicted_close_price = 0
def predict_price(ticker):
    """Prophet으로 당일 종가 가격 예측"""
    global predicted_close_price
    df = pyupbit.get_ohlcv(ticker, interval="minute60")
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]
    if len(closeDf) == 0:
        closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]
    closeValue = closeDf['yhat'].values[0]
    predicted_close_price = closeValue
predict_price("KRW-JST")
schedule.every().hour.do(lambda: predict_price("KRW-JST"))

# 시작 메세지 슬랙 전송
post_message(myToken,"#jst-coin", "autotrade start")
def job():
    post_message(myToken,"#jst-coin", predicted_close_price)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
