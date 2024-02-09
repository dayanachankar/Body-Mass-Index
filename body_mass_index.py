# -*- coding: utf-8 -*-
"""Body Mass Index.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e--nbU1mJJ7An2NseG4MdXL5mcxWBFP1

#Import Librabries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""#Import Dataset"""

BMI = pd.read_csv("/content/bmi.csv")
BMI

"""#Data Pre-Processing"""

#check dataset of rows & columns
BMI.shape

# check first 4 rows
BMI.head(4)

# check last 4 rows
BMI.tail()

# Getting some info abount dataset
BMI.info()

# Statistical measure
BMI.describe()

# check Missing values
BMI.isnull().sum()

# check duplicates
BMI.duplicated().sum()

# Duplictes values
BMI[BMI.duplicated()]

# Remove Duplicates
BMI.drop_duplicates(inplace=True)
BMI.shape

"""# Data Visualization"""

# BMI Counts - Index
plt.figure(figsize=(5, 5))
sns.countplot(x= 'Index',data =BMI ,palette='Set1')
plt.title("BMI Counts - Index")
plt.show()

# BMI Counts - Height
plt.figure(figsize=(25,10))
sns.countplot(x="Height",data=BMI,palette='Set1')
plt.title("BMI Counts - Height")
plt.show()

# BMI Counts - Weight
plt.figure(figsize=(35,15))
sns.countplot(x="Weight",data= BMI,palette = "Set1")
plt.title("BMI Counts - Weight")

# Gender
gender_counts = BMI['Gender'].value_counts()
gender_counts

plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index)
colors = ['skyblue', 'lightcoral']
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',colors=colors)
plt.title('Gender Distribution')
plt.show()

"""# Label Encoding"""

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
BMI['Gender'] = LE.fit_transform(BMI["Gender"])
BMI["Gender"].value_counts()

"""#Correlation"""

# Heatmap

BMI_corr = BMI.corr()
f, ax = plt.subplots(figsize=(6, 6))

sns.heatmap(BMI_corr, annot=True, fmt='.2f',cmap='Blues',annot_kws={'size': 10}, ax=ax)
plt.title('Correlation Heatmap')
plt.show()

# Correlations with "Index"

limit = -1.0

data = BMI.corr()["Index"].sort_values(ascending=False)
indices = data.index
labels = []
corr = []
for i in range(1, len(indices)):
    if data[indices[i]]>limit:
        labels.append(indices[i])
        corr.append(data[i])
sns.barplot(x=corr, y=labels)
plt.title('Correlations with "Index"')
plt.show()

# check the outliers
fig,ax = plt.subplots(figsize = (10,10))
boxplot = ax.boxplot(BMI.values,vert = False,labels=BMI.columns)
plt.xticks(ha ='right')
plt.title("Box Plots For Multiple Variables")
plt.xlabel('Values')
plt.ylabel('Variables')
plt.show()

"""There is no outlier in data

# Splitting dataset into target & features value
"""

X1 = BMI.drop(columns=['Index'],axis=1)
Y = BMI['Index']
X1

Y

from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
scaled_data = SS.fit_transform(X1)
X = pd.DataFrame(scaled_data, columns=X1.columns)
X

# Split dataset into train & test dataset
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.2,random_state=42)
print(X_train.shape,X_test.shape)
print(Y_train.shape,Y_test.shape)

"""# MODEL SELECTION"""

# MODEL - Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
log_model = LogisticRegression(multi_class='multinomial',solver='lbfgs')
log_model.fit(X_train, Y_train)

# accuracy on training data
X_train_prediction = log_model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('LogisticRegression - Accuracy on Training data : ', training_data_accuracy)


# accuracy on test data
X_test_prediction = log_model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('LogisticRegression - Accuracy score on Test Data : ', test_data_accuracy)

print("Classification Report:\n", classification_report(Y_test,X_test_prediction))
print("Confusion Matrix:\n", confusion_matrix(Y_test,X_test_prediction))

# MODEL - RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, Y_train)

# accuracy on training data
X_train_pred = model.predict(X_train)
training_data_accurancy = accuracy_score(X_train_pred, Y_train)
print('RandomForest - Accuracy on Training data : ', training_data_accuracy)


# accuracy on test data
X_test_pred = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_pred, Y_test)
print('RandomForest - Accuracy score on Test Data : ', test_data_accuracy)

print("Classification Report:\n", classification_report(Y_test,X_test_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test,X_test_pred))

# MODEL - SUPPORT VECTOR MACHINE
from sklearn import svm
classifier = svm.SVC(kernel='linear',gamma='auto',C=2)
classifier.fit(X_train,Y_train)

# accuracy on training data
X_train_pred1 = classifier.predict(X_train)
train_data_accurancy = accuracy_score(X_train_pred1, Y_train)
print('SVM - Accuracy on Training data : ', train_data_accurancy)


# accuracy on test data
X_test_pred1 = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_pred1, Y_test)
print('SVM - Accuracy score on Test Data : ', test_data_accuracy)

# MODEL - Decision Tree
from sklearn import tree
dtree = tree.DecisionTreeClassifier()
dtree.fit(X_train, Y_train)

# accuracy on training data
X_train_pred2 = dtree.predict(X_train)
training_data_accuracy = accuracy_score(X_train_pred2, Y_train)
print('Decision Tree - Accuracy on Training data : ', training_data_accuracy)


# accuracy on test data
X_test_pred2 = dtree.predict(X_test)
test_data_accuracy = accuracy_score(X_test_pred2, Y_test)
print('Decision Tree - Accuracy score on Test Data : ', test_data_accuracy)

print("Classification Report:\n", classification_report(Y_test,X_test_pred2))
print("Confusion Matrix:\n", confusion_matrix(Y_test,X_test_pred2))

# MODEL - k-Nearest Neighbors (kNN)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)

# accuracy on training data
X_train_pred3 = knn.predict(X_train)
train_accuracy = accuracy_score(X_train_pred3,Y_train)
print("KNN - Training Accuracy :", train_accuracy)

# accuracy on test data
X_test_pred3 = knn.predict(X_test)
test_accuracy = accuracy_score(X_test_pred3,Y_test)
print("KNN - Test Accuracy :", test_accuracy)

print("Classification Report:\n", classification_report(Y_test,X_test_pred3))
print("Confusion Matrix:\n", confusion_matrix(Y_test,X_test_pred3))

data = {
    'Model': ['Logistic Regression', 'Random Forest', 'Support Vector Machine (SVM)', 'Decision Tree', 'k-Nearest Neighbors (kNN)'],
    'Training Accuracy': [86.19, 86.19, 95.14, 100.00, 92.58],
    'Test Accuracy': [90.82, 84.69, 86.73, 80.61, 80.61]
}

df = pd.DataFrame(data)
df

"""The Logistic Regression model is a good fit for the dataset as it performs well on both the training and test data"""