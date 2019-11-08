import requests
# AlphaVantage Api Key: QGWWX3XZVW7STJJM
KEY = "QGWWX3XZVW7STJJM"
PARAMS = {'function':"TIME_SERIES_INTRADAY",
          'symbol':"MSFT",
          'interval':'60min',
          'apikey':KEY}
URL = "https://www.alphavantage.co/query"

NEWPARAMS = {'function':'SECTOR',
             'apikey':KEY
            }

r = requests.get(url = URL, params = NEWPARAMS)
data = r.json()
print(data);
