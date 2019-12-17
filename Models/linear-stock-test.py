from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import json
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

with open("../Data/companies.json") as file:
    # Load data from the json file
    data = json.load(file)

    # Obtain dates for the quarter using ordinal representation
    quarter_dates = []
    for x in data['companies'][0]['balance_sheet']:
        date_list = x['date'].split('-')
        date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        quarter_dates.append(date.toordinal())

    stocks = data['companies'][0]['stock_price']

    # Reverse all the dates in the list
    quarter_dates.reverse()
    stocks.reverse()
    
    # Reserve half of the date data for training and testing
    quarter_dates_train = np.array(quarter_dates[:-21])
    quarter_dates_test = np.array(quarter_dates[-21:])

    # Convert into a 2D array
    quarter_dates_train = quarter_dates_train[:, np.newaxis]
    quarter_dates_test = quarter_dates_test[:, np.newaxis]

    # Reserve half of the stock data for training and testing
    stocks_train = np.array(stocks[:-21])
    stocks_test = np.array(stocks[-21:])

    # Convert into a 2D array
    stocks_train = stocks_train[:, np.newaxis]
    stocks_test = stocks_test[:, np.newaxis]
    
    # Create linear regression object
    reg_mod = linear_model.LinearRegression()
    
    # Train the model using the training sets
    reg_mod.fit(quarter_dates_train, stocks_train)
    
    # Make predictions using the testing set
    stocks_prediction = reg_mod.predict(quarter_dates_test)
    
    # The coefficients
    print('Coefficients: \n', reg_mod.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
      % mean_squared_error(stocks_test, stocks_prediction))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(stocks_test, stocks_prediction))
    
    # Plot outputs
    plt.scatter(quarter_dates_test, stocks_test,  color='black')
    plt.plot(quarter_dates_test, stocks_prediction, color='blue', linewidth=3)
    
    plt.xticks(())
    plt.yticks(())
    
    plt.show()
