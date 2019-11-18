import pandas
import json
import Data.statements as statements

result = pandas.read_csv('SandP500Companies.csv')
data = {}
data['companies'] = []
for idx, symbol in enumerate(result['Symbol'][:3]):
    try:
        income = statements.income_statement(symbol)
        balance = statements.balance_sheet(symbol)
        cash_flow = statements.cash_flow(symbol)
        
        # Quarterly stock prices calculated, put into a json list.
        stock_price = []
        for entry in income:
            price = statements.quarterly_price(symbol, entry["date"])
            stock_price.append(price)
        
        company =   {'name':symbol, 'income_statement':income,
                    'balance_sheet': balance, 'cash_flow': cash_flow,
                    'stock_price': stock_price}
        data['companies'].append(company)
        print("Successfully read " + symbol + ", idx: " + str(idx))
    except Exception as e:
        print(e)
        print("Info not found for ticker: " + symbol, ", idx: ", str(idx))

# Writing json to data.txt
with open('companies.json', 'w') as outfile:
    json.dump(data, outfile)
