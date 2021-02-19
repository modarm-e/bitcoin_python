#REST API https://docs.upbit.com/reference
import requests

url = "https://api.upbit.com/v1/market/all"
params={
  "isDetails":"false"
}
resp = requests.get(url,params=params)
data= resp.json() #JSON

krw_tickers = []
for coin in data:
  ticker = coin['market'] #딕셔너리 key값으로 찾음
  
  if ticker.startswith('KRW'):
    krw_tickers.append(ticker)
    
print(len(krw_tickers))