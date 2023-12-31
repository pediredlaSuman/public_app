# -*- coding: utf-8 -*-
"""mdps_public

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m6NoAsWNWFaeSgsreBanKzo36zcufuaL
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
db_2=pd.read_csv('/content/Db_2.csv')
X = db_2.drop(columns = 'Outcome', axis=1)
Y = db_2['Outcome']
scaler=StandardScaler()
scaler.fit(X)
st_data = scaler.transform(X)
from sklearn.model_selection import train_test_split

# Split the data into training and combined validation/testing sets (80% train, 20% val/test)
X_train, X_val_test, Y_train, Y_val_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Split the combined validation/testing set into validation and testing sets (50% val, 50% test)
X_validation, X_test, Y_validation, Y_test = train_test_split(X_val_test, Y_val_test, test_size=0.5, stratify=Y_val_test, random_state=2)

# Print the shapes of the resulting sets
print("Shape of X_train:", X_train.shape)
print("Shape of X_validation:", X_validation.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of Y_train:", Y_train.shape)
print("Shape of Y_validation:", Y_validation.shape)
print("Shape of Y_test:", Y_test.shape)
 #training the support vector mechine Classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)
#adv:High Accuracy,Robustness to Overfitting
#dis:Sensitivity to Parameter Tuning,Limited Scalability