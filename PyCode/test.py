import time

import requests, json

header = {'Content-Type': 'application/json'}


r = requests.get('https://fapi.binance.com/fapi/v1/ticker/24hr?symbol=BTCUSDT', headers=header)
j = r.json()

print(j['priceChangePercent'])

