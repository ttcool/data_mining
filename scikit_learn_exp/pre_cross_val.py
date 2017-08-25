#coding: utf-8
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
import csv
import numpy as np


data_filename = "ionosphere.data"

X = np.zeros((351, 34), dtype='float')
y = np.zeros((351,), dtype='bool')



with open(data_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
        data = [float(datum) for datum in row[:-1]]
        X[i] = data
        y[i] = row[-1] == 'g'

#人为打乱数据，每隔一行，就把第二个特征的值除以10
X_broken = np.array(X)
X_broken[:,::2] /= 10



X_transformed = MinMaxScaler().fit_transform(X_broken)



for i in X_transformed:
    print X_transformed

estimator = KNeighborsClassifier()
scaling_pipeline = Pipeline([('scale', MinMaxScaler()),('predict', KNeighborsClassifier())])

avg_scores = []
all_scores = []
parameter_values = list(range(1, 21)) # Include 20
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(scaling_pipeline, X_broken, y, scoring='accuracy')
    average_accuracy = np.mean(scores) * 100
    print("The average accuracy is {0:.1f}%".format(average_accuracy))