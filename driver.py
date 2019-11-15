import pandas
import Data.statements as statements
result = pandas.read_csv('SandP500Companies.csv')
for symbol in result['Symbol'][:10]:
    try:
        income = statements.income_statement(symbol)
        print(symbol)
        print(income)
        print("")
    except:
        print("Info not found for ticker: " + symbol)
