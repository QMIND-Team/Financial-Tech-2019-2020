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
    quarter_dates = []
    revenue = []
    for x in data['companies'][1]['income_statement']:
        # Fetch date information
        date_list = x['date'].split('-')
        date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        quarter_dates.append(date.toordinal())

        # Fetch revenue information
        revenue.append(float(x['Revenue']))

    # Reverse all the dates in the list
    quarter_dates.reverse()
    revenue.reverse()

    # Split data for training and testing
    quarter_dates_train, quarter_dates_test, revenue_train, revenue_test = \
        train_test_split(np.array(quarter_dates), np.array(revenue), test_size=0.30)

    history = [x for x in revenue_train]

    predictions = list()
    for t in range(len(revenue_test)):
        # this model will be different on each iteration because we are appending our predictions to history
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = revenue_test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(revenue_test, predictions)
    print('Test MSE: %.3f' % error)

    # plot
    pyplot.plot(revenue_test, label="Actual values")
    pyplot.plot(predictions, color='red', label="Prediction")
    pyplot.xlabel("Date")
    pyplot.ylabel("Revenue ($ Billion)")
    pyplot.legend()
    pyplot.title("Revenue Prediction for the AEP ticker (ARIMA)")
    pyplot.show()
