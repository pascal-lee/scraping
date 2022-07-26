from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi2.csv")

#tbl.columns=["height","weight","label"]
print(list(tbl))
# print(tbl.head(10))
label = tbl["label"]
print(label.head(10))
w = tbl["weight"]/100
h = tbl["height"]/200
wh = pd.concat([w, h], axis= 1)
print(f"pre view:{wh.head(10)}")

data_train, data_test, label_train, label_test = train_test_split(wh,label)

# train data
clf = svm.SVC()
clf.fit(data_train, label_train)

# predict data
predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print(f"정답률={ac_score}")
print(f"리포트= \n {cl_report}")