# -*- coding: utf-8 -*-
"""building_classification_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N-KViIv_sazkCfY-41ytCtBOSwJo1uW9

# Building & Deploying a Machine Learning Classification model

## Import the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Read the dataset"""

dataset = pd.read_csv('https://raw.githubusercontent.com/futurexskill/ai/master/storepurchasedata.csv')

"""## Sample records"""

dataset.head(5)

"""## Get  dataset info"""

dataset.info()

"""## Get statistical info"""

dataset.describe()

"""## Feature selection

### Store the features (Age & Salary) in a NumPy array X
"""

X = dataset.iloc[:, :-1].values
X

"""## Store  the Dependent variaable in a NumPy Array"""

y = dataset.iloc[:,-1].values
y

"""## Exploratory Data Analysis using MatplotLib

### Plot Purchased Vs Age
"""

plt.scatter(X[:,0], y, color = 'blue')

"""### Plot Purchased Vs Salary"""

plt.scatter(X[:,1], y, color = 'red')

"""## Split the Training and Test Data"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =.20,random_state=0)

"""### Print the training set features (Independent Variables - Age, Salary)"""

X_train

"""### Print the training set dependent variable - Purchased"""

y_train

"""### Print the test set features (Independent Variables) - Age & Salary"""

X_test

"""### Print the test set dependent variable - Purchased"""

y_test

"""## Feature Scaling

StandardScaler will transform your data such that its distribution will have a mean value 0 and standard deviation of 1
"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""### Print feature scaled training independent variables"""

X_train

"""### Print feature scaled training independent variables"""

X_test

"""## Build a Classification model

### We are using KNN Classifier in this example

*n_neighbors = 5 -* Number of neighbors


*metric = 'minkowski', p = 2* - For Eucledian distance calculation
"""

from sklearn.neighbors import KNeighborsClassifier
# minkowski is for ecledian distance
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

"""## Train your Classifier

### This step is Machine Learning
"""

classifier.fit(X_train, y_train)

"""### Now "classifier" is your trained model

## Predict output for the test set
"""

y_pred = classifier.predict(X_test)
y_pred

y_test

"""## Predict probability"""

y_prob = classifier.predict_proba(X_test)[:,1]
y_prob

"""## Evaluate the Model"""

from sklearn.metrics import confusion_matrix

"""### Create Confusion Matrix"""

cm = confusion_matrix(y_test, y_pred)
cm

"""### Calculate Accuracy"""

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred))

"""### Derive the classification report

precision (true posistive / (true postive + false positive)) . It is the fraction of relevant instances among the retrieved instances

recall (true positive / (true postive + false negatives) ) . It is the fraction of relevant instances that have been retrieved over the total amount of relevant instances.

f1-score is weighted score of precision and recall.   2*((precision*recall)/(precision+recall))

The support is the number of samples of the true response that lie in that class
"""

from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

"""## Predict using the Model"""

new_prediction = classifier.predict(sc.transform(np.array([[40,20000]])))
new_prediction

new_prediction_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]
new_prediction_proba

new_pred = classifier.predict(sc.transform(np.array([[42,50000]])))
new_pred

new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]
new_pred_proba

"""## Store the Model & the Scaler"""

import pickle

filename = "knnmodel.pickle"

pickle.dump(classifier, open(filename,'wb'))

filename2 = "sc.pickle"

pickle.dump(sc, open(filename2,'wb'))

!ls

