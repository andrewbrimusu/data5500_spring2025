'''
This program queries coingecko for ethereum prices in USD
It only runs for one coin, ethereum
The urls require a specific date, and are generated using the datetime timedelta library, to handle things like leap year(s)
The data is written to a csv
'''

import requests
import json
import time
import os
from datetime import datetime, timedelta


# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=04-02-2025"


# url pieces, coin and date go in between  
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

date = "04-02-2025"
coin = "ethereum"

url = url1 + coin + url2 + date + url3
print(url)

# I need keys
md_key = "market_data"
current_key = "current_price"
btc_key = "btc"

# beautiful code
req = requests.get(url)
data = req.json()

print(data[md_key][current_key][btc_key])



