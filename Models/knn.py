import json
import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
# import matplotlib.pyplot as plt

with open("../Data/companies.json") as file:
    # Load data from the json file
    data = json.load(file)
    balance_sheet = pd.DataFrame(data=data['companies'][0]['balance_sheet'])
    del balance_sheet['date']
    income_statement = pd.DataFrame(data=data['companies'][0]['income_statement'])

    X = balance_sheet.values
    y = income_statement['Revenue'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print(classification_report(y_test, y_pred))
