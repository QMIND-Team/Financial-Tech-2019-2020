import pandas
import json
import Statements.statements as statements

result = pandas.read_csv('Data/companies.csv')
data = {}
data['companies'] = []
for idx, symbol in enumerate(result['Symbol'][:10]):
    try:
        income = statements.income_statement(symbol)
        balance = statements.balance_sheet(symbol)
        cash_flow = statements.cash_flow(symbol)
    except:
        print("Error with statements")
        print("Skipped company: " + str(symbol) + ", idx: " + str(idx))
        continue

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
with open('Data/companies.json', 'w') as outfile:
    json.dump(data, outfile)
