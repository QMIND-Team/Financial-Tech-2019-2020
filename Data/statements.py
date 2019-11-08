# Simple program that tries out the financialmodelprep API.
import requests

def income_statement(ticker):        
    url = "https://financialmodelingprep.com/api/v3/financials/income-statement/" + ticker
    resp = requests.get(url=url)
    output = resp.json()
    return output['financials']

def balance_sheet(ticker):
    url = "https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + ticker
    resp = requests.get(url=url)
    output = resp.json()
    return output['financials']

def cash_flow(ticker):
    url = "https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/" + ticker
    resp = requests.get(url=url)
    output = resp.json()
    return output['financials']

