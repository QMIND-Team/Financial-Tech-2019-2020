import pandas
import Data.statements as statements

result = pandas.read_csv('SandP500Companies.csv')
for symbol in result['Symbol'][:10]:
    try:
        income = statements.income_statement(symbol)
        for entry in income:
            price = statements.quarterly_price(symbol, entry["date"])
            entry["Quaterly Price"] = price
        print(symbol)
        print(income)
        print("")
    except:
        print("Info not found for ticker: " + symbol)
