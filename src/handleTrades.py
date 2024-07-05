import alpaca_trade_api as tradeapi
import requests
import config
import orderController

def shouldBuy():
    return True

def shouldSell():
    return True

def handleStock(stock = ''):
    if shouldBuy:
        orderController.createMarketOrder(stock)
        return 1
    elif shouldSell:
        orderController.sellMarketOrder(stock)
        return 1
    return 0


