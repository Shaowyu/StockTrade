import alpaca_trade_api as tradeapi
import requests
import config
from config import *
import orderController

print("Would you like to buy or sell a stock?")
type = input()
while type != 'buy' or type != 'sell':
    print("Error, please enter either 'buy' or 'sell'")
    type = input()
    if type == 'buy' or type == 'sell':
        break
print("Please enter the ticker symbol for the stock you would like to buy: ")
stock = input()
if type == 'buy':
    orderController.createMarketOrder(stock)
elif type == 'sell':
    orderController.sellMarketOrder(stock)




