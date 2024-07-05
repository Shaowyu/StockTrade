import alpaca_trade_api as tradeapi
import requests
import config
import orderController
import sys

api = tradeapi.REST(
    key_id = config.ALPACA_KEY,
    secret_key = config.ALPACA_SECRET_KEY,
    base_url = config.APCA_API_BASE_URL
)

def findHistoricMax(stock = ''):
    max = -1
    barset = api.get_barset(stock, 'day', limit = sys.maxint)
    for data in barset:
        if data > max:
            max = data
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


