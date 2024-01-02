import time
import pyupbit
import datetime

access = "p7r7Lc5Gi1uxRLQRLxTIQa98FBKIbw6Kw7tznhMx"
secret = "Pxsq7YBsKJUxQtq0AGjGW6Ny6lsUPXJ0fdEREfcx"

def get_open_price(ticker):
    """시가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    open_price = df.iloc[0]['open']
    return open_price
open_price_btc = get_open_price("KRW-BTC")
open_price_eth = get_open_price("KRW-ETH")
open_price_xrp = get_open_price("KRW-XRP")
open_price_ada = get_open_price("KRW-ADA")

 
def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma14(ticker):
    """14일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=14)
    ma14 = df['close'].rolling(14).mean().iloc[-1]
    return ma14

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)
        krw = get_balance("KRW")
        btc = get_balance("BTC")
        eth = get_balance("ETH")
        xrp = get_balance("XRP")
        ada = get_balance("ADA")
        # open_price_btc = get_open_price("KRW-BTC")
        # open_price_eth = get_open_price("KRW-ETH")
        # open_price_xrp = get_open_price("KRW-XRP")
        # open_price_ada = get_open_price("KRW-ADA")
    

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price_btc = get_target_price("KRW-BTC", 0.5)
            target_price_eth = get_target_price("KRW-ETH", 0.5)
            target_price_xrp = get_target_price("KRW-XRP", 0.5)
            target_price_ada = get_target_price("KRW-ADA", 0.5)
            ma14_btc = get_ma14("KRW-BTC")
            ma14_eth = get_ma14("KRW-ETH")
            ma14_xrp = get_ma14("KRW-XRP")
            ma14_ada = get_ma14("KRW-ADA")
            current_price_btc = get_current_price("KRW-BTC")
            current_price_eth = get_current_price("KRW-ETH")
            current_price_xrp = get_current_price("KRW-XRP")
            current_price_ada = get_current_price("KRW-ADA")
            if target_price_btc < current_price_btc and ma14_btc < current_price_btc:

                if krw > 5000 and btc == 0 and eth == 0 and xrp == 0 and ada == 0:   # 보유코인 0
                    upbit.buy_market_order("KRW-BTC", krw*0.2495)
                elif krw > 5000 and btc == 0 and eth > 0 and xrp == 0 and ada == 0:   # 보유코인 1
                    upbit.buy_market_order("KRW-BTC", krw*0.3325)
                elif krw > 5000 and btc == 0 and eth == 0 and xrp > 0 and ada == 0:
                    upbit.buy_market_order("KRW-BTC", krw*0.3325)
                elif krw > 5000 and btc == 0 and eth == 0 and xrp == 0 and ada > 0:
                    upbit.buy_market_order("KRW-BTC", krw*0.3325)
                elif krw > 5000 and btc == 0 and eth == 0 and xrp > 0 and ada > 0:   # 보유코인 2
                    upbit.buy_market_order("KRW-BTC", krw*0.4995)
                elif krw > 5000 and btc == 0 and eth > 0 and xrp == 0 and ada > 0:
                    upbit.buy_market_order("KRW-BTC", krw*0.4995)
                elif krw > 5000 and btc == 0 and eth > 0 and xrp > 0 and ada == 0:
                    upbit.buy_market_order("KRW-BTC", krw*0.4995)
                elif krw > 5000 and btc == 0 and eth > 0 and xrp > 0 and ada > 0:   # 보유코인 3
                    upbit.buy_market_order("KRW-BTC", krw*1)

            if target_price_eth < current_price_eth and ma14_eth < current_price_eth:

                if krw > 5000 and eth == 0 and btc == 0 and xrp == 0 and ada == 0:   # 보유코인 0
                    upbit.buy_market_order("KRW-ETH", krw*0.2495)
                elif krw > 5000 and eth == 0 and btc > 0 and xrp == 0 and ada == 0:   # 보유코인 1
                    upbit.buy_market_order("KRW-ETH", krw*0.3325)
                elif krw > 5000 and eth == 0 and btc == 0 and xrp > 0 and ada == 0:
                    upbit.buy_market_order("KRW-ETH", krw*0.3325)
                elif krw > 5000 and eth == 0 and btc == 0 and xrp == 0 and ada > 0:
                    upbit.buy_market_order("KRW-ETH", krw*0.3325)
                elif krw > 5000 and eth == 0 and btc == 0 and xrp > 0 and ada > 0:   # 보유코인 2
                    upbit.buy_market_order("KRW-ETH", krw*0.4995)
                elif krw > 5000 and eth == 0 and btc > 0 and xrp == 0 and ada > 0:
                    upbit.buy_market_order("KRW-ETH", krw*0.4995)
                elif krw > 5000 and eth == 0 and btc > 0 and xrp > 0 and ada == 0:
                    upbit.buy_market_order("KRW-ETH", krw*0.4995)
                elif krw > 5000 and eth == 0 and btc > 0 and xrp > 0 and ada > 0:   # 보유코인 3
                    upbit.buy_market_order("KRW-ETH", krw*1)

            if target_price_xrp < current_price_xrp and ma14_xrp < current_price_xrp:

                if krw > 5000 and xrp == 0 and btc == 0 and eth == 0 and ada == 0:   # 보유코인 0
                    upbit.buy_market_order("KRW-XRP", krw*0.2495)
                elif krw > 5000 and xrp == 0 and btc > 0 and eth == 0 and ada == 0:   # 보유코인 1
                    upbit.buy_market_order("KRW-XRP", krw*0.3325)
                elif krw > 5000 and xrp == 0 and btc == 0 and eth > 0 and ada == 0:
                    upbit.buy_market_order("KRW-XRP", krw*0.3325)
                elif krw > 5000 and xrp == 0 and btc == 0 and eth == 0 and ada > 0:
                    upbit.buy_market_order("KRW-XRP", krw*0.3325)
                elif krw > 5000 and xrp == 0 and btc == 0 and eth > 0 and ada > 0:   # 보유코인 2
                    upbit.buy_market_order("KRW-XRP", krw*0.4995)
                elif krw > 5000 and xrp == 0 and btc > 0 and eth == 0 and ada > 0:
                    upbit.buy_market_order("KRW-XRP", krw*0.4995)
                elif krw > 5000 and xrp == 0 and btc > 0 and eth > 0 and ada == 0:
                    upbit.buy_market_order("KRW-XRP", krw*0.4995)
                elif krw > 5000 and xrp == 0 and btc > 0 and eth > 0 and ada > 0:   # 보유코인 3
                    upbit.buy_market_order("KRW-XRP", krw*1)

            if target_price_ada < current_price_ada and ma14_ada < current_price_ada:

                if krw > 5000 and ada == 0 and btc == 0 and eth == 0 and xrp == 0:   # 보유코인 0
                    upbit.buy_market_order("KRW-ADA", krw*0.2495)
                elif krw > 5000 and ada == 0 and btc > 0 and eth == 0 and xrp == 0:   # 보유코인 1
                    upbit.buy_market_order("KRW-ADA", krw*0.3325)
                elif krw > 5000 and ada == 0 and btc == 0 and eth > 0 and xrp == 0:
                    upbit.buy_market_order("KRW-ADA", krw*0.3325)
                elif krw > 5000 and ada == 0 and btc == 0 and eth == 0 and xrp > 0:
                    upbit.buy_market_order("KRW-ADA", krw*0.3325)
                elif krw > 5000 and ada == 0 and btc == 0 and eth > 0 and xrp > 0:   # 보유코인 2
                    upbit.buy_market_order("KRW-ADA", krw*0.4995)
                elif krw > 5000 and ada == 0 and btc > 0 and eth == 0 and xrp > 0:
                    upbit.buy_market_order("KRW-ADA", krw*0.4995)
                elif krw > 5000 and ada == 0 and btc > 0 and eth > 0 and xrp == 0:
                    upbit.buy_market_order("KRW-ADA", krw*0.4995)
                elif krw > 5000 and ada == 0 and btc > 0 and eth > 0 and ada > 0:   # 보유코인 3
                    upbit.buy_market_order("KRW-ADA", krw*1)
            
            if open_price_btc > current_price_btc and btc > 0:
                upbit.sell_market_order("KRW-BTC", btc*1)

            if open_price_eth > current_price_eth and eth > 0:
                upbit.sell_market_order("KRW-ETH", eth*1)

            if open_price_xrp > current_price_xrp and xrp > 0:
                upbit.sell_market_order("KRW-XRP", xrp*1)

            if open_price_ada > current_price_ada and ada > 0:
                upbit.sell_market_order("KRW-ADA", ada*1)

        else:
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*1)
            elif eth > 0.00008:
                upbit.sell_market_order("KRW-ETH", eth*1)
            elif xrp > 0.00008:
                upbit.sell_market_order("KRW-XRP", xrp*1)
            elif ada > 0.00008:
                upbit.sell_market_order("KRW-ADA", ada*1)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
