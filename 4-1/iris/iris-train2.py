from sklearn import svm, metrics
import random, re
import pandas as pd
from sklearn.model_selection import train_test_split

# load csv data
csv = pd.read_csv('iris.csv')

# data vs label
print(csv.columns.values)
csv_data = csv.iloc[:,0:4]
csv_label = csv.iloc[:,4]
# print(f" data: {csv_data.head(10)}")
# print(f" data: {csv[['SepalLength' ,'SepalWidth' ,'PetalLength' ,'PetalWidth']]}")
# print(f" data: {csv_label.head(10)}")

train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# train data
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

# accuracy
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률: {ac_score}")
