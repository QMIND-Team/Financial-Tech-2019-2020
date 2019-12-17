# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

from sklearn.neighbors import KNeighborsClassifier

# get the data
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# make the model
neigh = KNeighborsClassifier(n_neighbors=3)

# train the model
neigh.fit(X, y)

print(neigh.predict([[1.1]]))

print(neigh.predict_proba([[0.9]]))