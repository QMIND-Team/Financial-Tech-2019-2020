import statements as statements
import matplotlib.pyplot as plt

result = statements.sector_info()
for entry in result:
    print(entry)
    print("-------------")

"""Plot the historical close prices"""
plotResults = statements.stock_price("AAPL", "2018-03-12", "2019-11-12")
plt.plot([entry['close'] for entry in plotResults])
plt.ylabel("Price")
plt.xlabel("Year")
plt.show()