# Simple program that tries out the financialmodelprep API.

import requests

statements = {'1':"income-statement", '2':"balance-sheet-statement", 
              '3':"cash-flow-statement"}
company = input("Enter the ticker for the company. (ex: AAPL): ")
statement_n = input("Enter the type of statement you would like (1 for income, 2 for balance sheet, 3 for cash flow): ")

url = "https://financialmodelingprep.com/api/v3/financials/" + statements[statement_n] + "/" + company
print(url)

resp = requests.get(url=url) 
output = resp.json()
print(output["symbol"])
for entry in output["financials"]:
    print(entry)
    print("------------------------")

