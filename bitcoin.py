import pyupbit
import pprint

# tickers = pyupbit.get_tickers(fiat="KRW")
# print(len(tickers))

# df = pyupbit.get_ohlcv("KRW-BTC","minute3",3) #분봉
# print(df)

# wf = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week",count=3) #주봉
# print(wf)

# nf = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day",count=7) #일봉
# print(nf)

# mf = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="month", count=12) #월봉
# print(mf)

# tickers = pyupbit.get_tickers(fiat="KRW") #원화 거래 현재가
# price = pyupbit.get_current_price(tickers)
# for k, v in price.items():
#   print(k,v)
"""
KRW-BTC 56166000.0
KRW-ETH 2003000.0
"""

#호가 정보
# import pprint
# orderbooks = pyupbit.get_orderbook("KRW-BTC")
# orderbook = orderbooks[0]

# total_ask_size = orderbook['total_ask_size']
# total_bid_size = orderbook['total_bid_size']

# print("매도호가 총합: ",total_ask_size)
# print("매수호가 총합: ",total_bid_size)


#로그인 exchange API 계정
f = open('E:\\Python\\bitcoin\\upbit.txt' , "r")
lines = f.readlines()
access = lines[0].strip() # '\n'제거하기위해 .strip() 사용
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret) # class instance, object
# balance = upbit.get_balance("KRW")
# print(balance , type(balance))
"""221.94243326 ㅠㅠ츄팝츄스도 못사"""

#잔고조회
# balances = upbit.get_balances() #list 리턴인데??
# pprint.pprint(balances[0])
""" 
{
'avg_buy_price': '0',
'avg_buy_price_modified': True,
'balance': '221.94243326',
'currency': 'KRW',
'locked': '0.0',
'unit_currency': 'KRW'
}
"""


#지정가 주문 #buy_limit_order()
# btc_price = pyupbit.get_current_price("KRW-BTC")
# print(btc_price)

# resp = upbit.buy_limit_order("KRW-BTC",100,1) #티커 , 주문가격, 주문량
# pprint.pprint(resp)
#uuid: 고유 주문 정보 -> 취소할때 사용 cancel.oreder()

#지정가 매도 주문 #sell_limit_order()
#bit_balance = upbit.get_balance("KRW_BTC") #소유 갯수 있는지
#resp = upbit.sell_limit_order("KRW-BTC",가격,bit_balance) # 티커, 주문가격, 주문량
#pprint.pprint(resp)


#시장가 주문 #buy_market_order(티커, 주문가격(원화))
# resp = upbit.buy_market_order("KRW-BTC", 200)
# pprint.pprint(resp)

#시장가 매도 #sell_market_order(티커, 주문량)
# balance= upbit.get_balance("KRW-BTC") #코인갯수
# resp = upbit.sell_market_order("KRW-BTC",balance)
# pprint.pprint(resp)

#주문취소 #cancel_order(uuid="~")
# resp = upbit.buy_limit_order("KRW-BTC",200,100) #구매
# print(resp[0]['uuid'])

# uuid=resp[0]['uuid'] #취소
# resp = upbit.cancel_order(uuid)
# pprint.pprint(resp)


#변동성 돌파 전략
""" 
레인지 계산 : 전일 고가 - 전일 저가 (하루안에 움직인 가격의 최대 폭) 9시
매수 기준: 시가 기준으로 가격이 '레인지*k'이상 상승하면 해당 가격에 매수
k는 0.5~1 중 선택해서 사용 (0.5)
매도 기준: 그날 종가에 판다
"""

""" 
각 거래일별 수익률 계산
매수한 경우의 수익률: 매도가 / 매수가 => 종가 / 목표가
매수하지 않은 수익률: 1 (원금 유지)
"""