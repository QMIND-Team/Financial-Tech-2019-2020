import pandas
import json
import Statements.statements as statements

result = pandas.read_csv('Data/companies.csv')
data = {'companies': []}

for idx in range(len(result['Symbol'])):
    symbol = result['Symbol'][idx]
    industry = result['GICS�Sector'][idx]

    # Passes entry if the company is not listed under Utilities
    if industry != "Utilities":
        continue

    # Checks to make sure the company's statements exist
    try:
        income = statements.income_statement(symbol)
        balance = statements.balance_sheet(symbol)
        cash_flow = statements.cash_flow(symbol)
    except:
        print("Couldn't find statements for: " + str(symbol) + ", idx: " + str(idx))
        continue

    # Quarterly stock prices calculated, put into a json list.
    stock_price = []
    for index, entry in enumerate(income):
        try:
            price = statements.quarterly_price(symbol, entry["date"])
            stock_price.append(price)
        except:
            print("Error with " + str(symbol) + ", date: " + entry["date"])

    # Catch to check if all lists are the same length
    if (len(income) == len(balance) and len(income) == len(cash_flow) and len(income) == len(stock_price)):
        # Saving the company to companies
        company =   {'name':symbol,
                'income_statement':income,
                'balance_sheet': balance,
                'cash_flow': cash_flow,
                'stock_price': stock_price
                }
        data['companies'].append(company)

        print("Successfully read " + symbol + ", idx: " + str(idx))
    else:
        print('Uneven data lengths for ' + symbol + ", idx:" + str(idx))

# Writing json to data.txt
with open('Data/companies.json', 'w') as outfile:
    json.dump(data, outfile)
