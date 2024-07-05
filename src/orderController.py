import alpaca_trade_api as tradeapi
import requests
import config

ORDERS_URL = '{}/v2/orders'.format(config.APCA_API_BASE_URL)

def createMarketOrder(ticker, qty, ordertype):
    side = 'buy'

    data = {
        'symbol' : ticker,
        'qty' : qty,
        'side' : side,
        'type' : ordertype,
        'time_in_force' : 'day'
    }

    r = requests.post(ORDERS_URL, json=data, headers=config.HEADERS)
    return r.content

def sellMarketOrder(ticker, qty, ordertype):
    side = 'sell'
    
    data = {
        'symbol' : ticker,
        'qty' : qty,
        'side' : side,
        'type' : ordertype,
        'time_in_force' : 'day'
    }

    r = requests.post(ORDERS_URL, json=data, headers=config.HEADERS)
    return r.content

def createLimitOrder(ticker, qty, ordertype, limitPrice):
    side = 'buy'

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
