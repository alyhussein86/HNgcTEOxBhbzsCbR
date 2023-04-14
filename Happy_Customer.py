
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn import linear_model
from sklearn.metrics import confusion_matrix

reader = pd.read_csv("ACME-HappinessSurvey2020.csv")

# data as X, Target as Y

# dropping column Y as it's the target and assigning Data as X
X = reader.drop(columns=['Y', 'X3', 'X6'])
y = reader['Y']  # assiging target as Y

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

# Normalizing data
ss_train = StandardScaler()
X_train = ss_train.fit_transform(X_train)

ss_test = StandardScaler()
X_test = ss_test.fit_transform(X_test)

# applying Regression

regmodel = linear_model.LogisticRegression()  # tree.DecisionTreeRegressor()
regmodel.fit(X, y)

predictions = regmodel.predict(X_test)

cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = cm.ravel()  # confusion_matrix(y_test, predictions).ravel()

print('True Positive(TP)  = ', TP)
print('False Positive(FP) = ', FP)
print('True Negative(TN)  = ', TN)
print('False Negative(FN) = ', FN)

accuracy = (TP + TN) / (TP + FP + TN + FN)

print('Accuracy of the binary classifier = {:0.3f}'.format(accuracy))

# print X as Data and Y as Target
# print(X.head())
# print(y.value_counts())

# sns.heatmap(reader, cbar=False, cmap='tab20c_r')
# plt.title('Missing Data: Training Set')
# plt.show()
