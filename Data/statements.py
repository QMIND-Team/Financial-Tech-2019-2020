# Simple program that tries out the financialmodelprep API.
import requests
from datetime import datetime
from datetime import timedelta
statement_params = {'period': 'quarter'}


def income_statement(ticker):
    url = "https://financialmodelingprep.com/api/v3/financials/income-statement/" + ticker
    resp = requests.get(url=url, params=statement_params)
    output = resp.json()
    return output['financials']


def balance_sheet(ticker):
    url = "https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + ticker
    resp = requests.get(url=url, params=statement_params)
    output = resp.json()
    return output['financials']


def cash_flow(ticker):
    url = "https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/" + ticker
    resp = requests.get(url=url, params=statement_params)
    output = resp.json()
    return output['financials']


# start and end are formatted as yyyy-mm-dd
def stock_price(ticker, start, end):
    url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + ticker
    time_param = {'from': start, 'to': end}
    resp = requests.get(url=url, params=time_param)
    output = resp.json()
    return output['historical']


def sector_info():
    url = "https://financialmodelingprep.com/api/v3/stock/sectors-performance"
    resp = requests.get(url=url)
    output = resp.json()
    return output['sectorPerformance']


def quarterly_price(ticker, date):
    dateList = date.split("-")
    realDate = datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]))
    realStart = realDate - timedelta(days=20)
    realEnd = realDate + timedelta(days=20)
    start = realStart.strftime("%Y-%m-%d")
    end = realEnd.strftime("%Y-%m-%d")
    priceResults = stock_price(ticker, start, end)
    quarterTotal = 0
    for entry in priceResults:
        quarterTotal += entry['close']
    quarterprice = quarterTotal/len(priceResults)
    return quarterprice
