from binance.client import Client
from binance.enums import *
import random
import time
import yaml

def buy_coin(currency, currency_quantity):
    order = client.order_market_buy(
    symbol= currency + 'USDT',
    quantity=currency_quantity)

def define_quantity(coin, avg_price):
    if coin == 'BTC':
        return round(dca_usdt_value / avg_price, 5)
    elif coin == 'ETH':
        return round(dca_usdt_value / avg_price, 4)
    elif coin == 'BNB':
        return round(dca_usdt_value / avg_price, 3)

def load_config(file):
    with open(file) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def create_file():
    with open('logs.txt', 'a+') as f:
        f.write('This is a log file for DCA trading bot\n')
        f.write('\n')

def log_order(action):
    with open('logs.txt', 'a+') as f:
        f.write(action + '\n')

config = load_config('config.yml')

API_KEY = config['API_KEY'] # Your public api key goes here
API_SECRET = config['API_SECRET'] # And your secret key goes here (don't show it to anybody!)

client = Client(API_KEY, API_SECRET)



#CONFIG:
coins = ['BTC', 'ETH', 'BNB'] # Coins for the next trade are going to be randomly chosen from this list
dca_periods = {'day': 86400, '3 days': 259200, 'week': 604800, 'month': 2_419_200}
dca_usdt_value = config['DCA_USDT_VALUE']
dca_period = config['DCA_PERIOD']


def main():
    create_file()
    while True:
        try:
            coin = random.choice(coins)
            avg_price = round(float(client.get_avg_price(symbol=coin + 'USDT')['price']))
            quantity = define_quantity(coin, avg_price)
            action = f'BUYING {quantity} {coin} for {dca_usdt_value} USDT with a price of {avg_price} {coin}/USDT. Next trade in a {dca_period} period'
            print(action)
            buy_coin(coin, quantity)
            log_order(action)
        except Exception as e:
            print(e)
            print('Some error occured.')
        time.sleep(dca_periods[dca_period])



if __name__ == '__main__':
    main()





