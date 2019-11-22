import Data.statements as statements

result = statements.sector_info()
for entry in result:
    print(entry)
    print("-------------")

# Plot the historical close prices
statements.plot_stock("AAPL", "2018-03-12", "2019-11-12")
