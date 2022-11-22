import time
import bybit
from pybit import inverse_perpetual
import csv

client = bybit.bybit(test = False, api_key='', api_secret='')


# Get Wallet Balance
result = client.Wallet.Wallet_getBalance(coin="BTC").result()[0]['result']['BTC']
print(result)


with open('./bybitBTC.csv', 'w') as f:
    w = csv.DictWriter(f, result)
    w.writeheader()
    w.writerow(result)

# Wallet Fund Records
result2 = client.Wallet.Wallet_getRecords().result()[0]['result']['data'][0]
print(result2)

with open('./bybitFundRec.csv', 'w') as f:
  w = csv.DictWriter(f, result2)
  w.writeheader()
  w.writerow(result2)

# Withdraw Records
result3=client.Wallet.Wallet_withdraw().result()[0]
print(result3)
with open('./bybitWithRec.csv', 'w') as f:
  w = csv.DictWriter(f, result3)
  w.writeheader()
  w.writerow(result3)

#withdraw_records()

result4= inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key=" ",
    api_secret=" ")
print(result4.user_trade_records(
    symbol="BTCUSD"))

with open('./bybitTradeRec.csv', 'w') as f:
  w = csv.DictWriter(f, result4.user_trade_records(
    symbol="BTCUSD"))
  w.writeheader()
  w.writerow(result4.user_trade_records(
    symbol="BTCUSD"))




