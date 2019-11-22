import pandas
import json
import Data.statements as statements

result = pandas.read_csv('SandP500Companies.csv')
data = {}
data['companies'] = []
for idx, symbol in enumerate(result['Symbol']):
    try:
        income = statements.income_statement(symbol)
        balance = statements.balance_sheet(symbol)
        cash_flow = statements.cash_flow(symbol)
    except:
        print("Error with statements")
        print("Skipped company: " + str(symbol) + ", idx: " + str(idx))

    # Quarterly stock prices calculated, put into a json list.
    stock_price = []
    for entry in income:
        try:
            price = statements.quarterly_price(symbol, entry["date"])
            stock_price.append(price)
        except:
            print("    Error with " + str(symbol) + ", date: " + entry["date"])
        
    # Saving the company to companies    
    company =   {'name':symbol, 'income_statement':income,
                'balance_sheet': balance, 'cash_flow': cash_flow,
                'stock_price': stock_price}
    data['companies'].append(company)
    print("Successfully read " + symbol + ", idx: " + str(idx))

# Writing json to data.txt
with open('companies.json', 'w') as outfile:
    json.dump(data, outfile)
