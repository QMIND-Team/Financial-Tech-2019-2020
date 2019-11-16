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
    date_list = date.split("-")
    date_mid = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    start = date_mid - timedelta(days=20)
    end = date_mid + timedelta(days=20)
    prices = stock_price(ticker, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))

    quarter_total = 0.0
    for entry in prices:
        quarter_total += entry['close']

    quarter_price = quarter_total / len(prices)
    return quarter_price
