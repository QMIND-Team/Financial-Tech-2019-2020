from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

with open("../Data/companies.json") as file:
    # Load data from the json file
    data = json.load(file)

    # Obtain dates for the quarter using ordinal representation
    quarter_dates = []
    for x in data['companies'][1]['balance_sheet']:
        date_list = x['date'].split('-')
        date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        quarter_dates.append(date.toordinal())

    stocks = data['companies'][1]['stock_price']

    # Reverse all the dates in the list
    quarter_dates.reverse()
    stocks.reverse()

    # Split data for training and testing
    quarter_dates_train, quarter_dates_test, stocks_train, stocks_test = \
        train_test_split(np.array(quarter_dates), np.array(stocks), test_size=0.30)

    # Convert into 2D arrays
    quarter_dates_train = quarter_dates_train[:, np.newaxis]
    quarter_dates_test = quarter_dates_test[:, np.newaxis]
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
    plt.scatter(quarter_dates_test, stocks_test, color='black', label="Actual values")
    plt.plot(quarter_dates_test, stocks_prediction, color='blue', label="Prediction")
    plt.xlabel("Date")
    plt.ylabel("Stock Price ($)")
    plt.legend()
    plt.title("Stock Price Prediction for the AEP ticker (Linear Regression)")
    plt.show()
