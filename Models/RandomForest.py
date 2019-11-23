# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

# this is just getting the data from the interweb
X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)

# make the model
regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)

# train the model
regr.fit(X, y)

print(regr.feature_importances_)

print(regr.predict([[0, 0, 0, 0]]))