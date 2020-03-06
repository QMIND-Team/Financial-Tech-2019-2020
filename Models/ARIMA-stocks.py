from datetime import datetime
import numpy as np
import json
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

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

    history = [x for x in stocks_train]

    predictions = list()
    for t in range(len(stocks_test)):
        # this model will be different on each iteration because we are appending our predictions to history
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = stocks_test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(stocks_test, predictions)
    print('Test MSE: %.3f' % error)

    # plot
    pyplot.plot(stocks_test, label="Actual values")
    pyplot.plot(predictions, color='red', label="Prediction")
    pyplot.xlabel("Date")
    pyplot.ylabel("Stock Price ($)")
    pyplot.legend()
    pyplot.title("Stock Price Prediction for the AEP ticker (ARIMA)")
    pyplot.show()
