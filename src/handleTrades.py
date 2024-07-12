import alpaca_trade_api as tradeapi
import requests
import config
import orderController
import sys
from datetime import date
import datetime
import pytz
import openai


openai.my_api_key = config.OPENAI_API_KEY
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

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
    potential = 40 * (findHistoricMax(stock) - api.get_latest_quote(stock).bp) / findHistoricMax(stock)
    
    message = "From articles within the last week of" + stock + "rate how the company's stock will perform on a scale from 0 to 60. Please only respond with a number and nothing else."
    messages.append( 
            {"role": "user", "content": message}, 
        ) 
    chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    potentialFromNews = int(reply)
    potential = potential + potentialFromNews

    if potential > 70:
        return True
    return False

def shouldSell(stock = ''):
    potential = 40 * (findHistoricMax(stock) - api.get_latest_quote(stock).bp) / findHistoricMax(stock)
    
    message = "From articles within the last week of" + stock + "rate how the company's stock will perform on a scale from 0 to 60. Please only respond with a number and nothing else."
    messages.append( 
            {"role": "user", "content": message}, 
        ) 
    chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    potentialFromNews = int(reply)
    potential = potential + potentialFromNews
    
    if potential < 30:
        return True
    return False

def handleStock(stock = ''):
    if shouldBuy(stock):
        orderController.createMarketOrder(stock)
        return 1
    elif shouldSell(stock):
        orderController.sellMarketOrder(stock)
        return 1
    return 0


print(shouldBuy('AAPL'))
