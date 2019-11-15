import pandas
import Data.statements as statements
result = pandas.read_csv('SandP500Companies.csv')
for symbol in result['Symbol']:
    print(symbol)
    print(statements.income_statement(symbol))
    print("")
