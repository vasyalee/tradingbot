from binance.client import Client
from binance.enums import *
import random
import time

API_KEY = '' # Your public api key goes here
API_SECRET = '' # And your secret key goes here (don't show it to anybody!)

client = Client(API_KEY, API_SECRET)

#CONFIG:
coins = ['BTC', 'ETH', 'BNB'] # Coins for the next trade are going to be randomly chosen from this list
dca_usdt_value = 12 # Here you can set the amount of USDT that is going to be regularly used for trades
dca_periods = {'day': 86400, '3 days': 259200, 'week': 604800, 'month': 2_419_200}


def main():
    while True:
        try:
            coin = random.choice(coins)
            avg_price = client.get_avg_price(symbol=coin + 'USDT')['price']
            quantity = dca_usdt_value / avg_price
            print(f'BUYING {coin}')
            buy_coin(coin, quantity)
        except Exception as e:
            print(e)
            print('Some error occured. This is probably because your balance is insufficient.')
        time.sleep(dca_periods['week'])

def buy_coin(currency, currency_quantity):
    order = client.order_market_buy(
    symbol= currency + 'USDT',
    quantity=currency_quantity)

if __name__ == '__main__':
    main()




