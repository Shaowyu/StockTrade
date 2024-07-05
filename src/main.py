import alpaca_trade_api as tradeapi
import requests
import config
from config import *


ORDERS_URL = '{}/v2/orders'.format(config.APCA_API_BASE_URL)

def createMarketOrder():
    ticker = 'AAPL'
    qty = '2'
    side = 'buy'
    ordertype = 'market'

    data = {
        'symbol' : ticker,
        'qty' : qty,
        'side' : side,
        'type' : ordertype,
        'time_in_force' : 'day'
    }

    r = requests.post(ORDERS_URL, json=data, headers=config.HEADERS)
    return r.content

def createLimitOrder():
    ticker = 'AAPL'
    qty = '2'
    side = 'buy'
    ordertype = 'market'
    limitPrice = '140'

    data = {
        'symbol' : ticker,
        'qty' : qty,
        'side' : side,
        'type' : ordertype,
        'time_in_force' : 'day',
        'limit_price' : limitPrice
    }

    r = requests.post(ORDERS_URL, json=data, headers=config.HEADERS)
    return r.content
print(createMarketOrder())