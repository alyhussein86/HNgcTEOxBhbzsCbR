import pandas as pd
from sklearn import linear_model

reader = pd.read_csv("ACME-HappinessSurvey2020.csv")

y = reader['Y']
X = reader[['X1', 'X2', 'X3', 'X4', 'X5', 'X6']]

regr = linear_model.LinearRegression()
regr.fit(X, y)

predicted = regr.predict([[1, 1, 1, 1, 1, 1]])
#  , 2, 1, 1, 5
print(predicted*100)
