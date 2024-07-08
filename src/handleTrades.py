import alpaca_trade_api as tradeapi
import requests
import config
import orderController
import sys
from datetime import date
import datetime
import pytz

api = tradeapi.REST(
    key_id = config.ALPACA_KEY,
    secret_key = config.ALPACA_SECRET_KEY,
    base_url = config.APCA_API_BASE_URL
)

def findHistoricMax(stock = ''):
    curDate = datetime.datetime.now(pytz.timezone('US/Eastern'))
    lastYear = curDate - datetime.timedelta(days=365)

    bars = api.get_bars(stock, '1Day', start = lastYear.isoformat(), end = None, limit = 365)
    max = -1
    for bar in bars:
        if bar.c > max:
            max = bar.c
    return max

def shouldBuy(stock = ''):
    return True

def shouldSell(stock = ''):
    return True

def handleStock(stock = ''):
    if shouldBuy(stock):
        orderController.createMarketOrder(stock)
        return 1
    elif shouldSell(stock):
        orderController.sellMarketOrder(stock)
        return 1
    return 0

print(findHistoricMax('AAPL'))
