import pandas
result = pandas.read_csv('./example.csv', names=['Symbol', 'Security', 'GISC Sector', 'GISC Sub Industry'])
print(result)
