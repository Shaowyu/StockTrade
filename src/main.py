import alpaca_trade_api as tradeapi
import requests
import config
from config import *
import orderController
import handleTrades

print("Would you like to buy or sell a stock?")
type = input()
if type != 'buy' and type != 'sell':
    while type != 'buy' or type != 'sell':
        print("Error, please enter either 'buy' or 'sell'")
        type = input()
        if type == 'buy' or type == 'sell':
            break
print("Please enter the ticker symbol for the stock you would like to buy: ")
stock = input()
if type == 'buy':
    if(not handleTrades.shouldBuy(stock)):
        print("This stock is not recommended to buy. Are you sure you would like to buy it?")
        print("Yes or No")
        answer = input()
        while answer != 'Yes' or answer != 'No':
            print("Error, please enter either 'Yes' or 'No'")
            type = input()
            if type == 'Yes' or type == 'No':
                break
    print("How many would you like to buy?")
    qty = input()
    print("What order type?")
    ordertype = input()
    if handleTrades.shouldBuy(stock) or answer == "Yes":
        orderController.createMarketOrder(stock, qty, ordertype)
elif type == 'sell':
    if(not handleTrades.shouldSell(stock)):
        print("This stock is not recommended to sell. Are you sure you would like to sell it?")
        print("Yes or No")
        answer = input()
        while answer != 'Yes' or answer != 'No':
            print("Error, please enter either 'Yes' or 'No'")
            type = input()
            if type == 'Yes' or type == 'No':
                break
    print("How many would you like to buy?")
    qty = input()
    print("What order type?")
    ordertype = input()
    if handleTrades.shouldSell(stock) or answer == "Yes" :
        orderController.sellMarketOrder(stock, qty, ordertype)




