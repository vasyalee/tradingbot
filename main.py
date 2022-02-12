from binance.client import Client
from binance.enums import *
import random
import time

API_KEY = '' # Your public api key goes here
API_SECRET = '' # And your secret key goes here (don't show it to anybody!)

client = Client(API_KEY, API_SECRET)

#CONFIG:
coins = ['BTC', 'ETH', 'BNB'] # Coins for the next trade are going to be randomly chosen from this list
dca_usdt_value = 10000 # Here you can set the amount of USDT that is going to be regularly used for trades
dca_periods = {'day': 86400, '3 days': 259200, 'week': 604800, 'month': 2_419_200}
dca_period = 'week' #Choose the DCA period. "Week" by default


def main():
    while True:
        try:
            coin = random.choice(coins)
            avg_price = round(float(client.get_avg_price(symbol=coin + 'USDT')['price']))
            quantity = round(dca_usdt_value / avg_price, 5)
            print(f'BUYING {quantity} {coin} for {dca_usdt_value} USDT with a price of {avg_price} {coin}/USDT. Next trade in {dca_period}')
            buy_coin(coin, quantity)
        except Exception as e:
            print(e)
            print('Some error occured. This is probably because your balance is insufficient.')
        time.sleep(dca_periods[dca_period])

def buy_coin(currency, currency_quantity):
    order = client.order_market_buy(
    symbol= currency + 'USDT',
    quantity=currency_quantity)

if __name__ == '__main__':
    main()





