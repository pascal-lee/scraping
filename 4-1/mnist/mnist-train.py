import pandas as pd
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split


# csv file loading

def load_csv(file_name):
    labels = []
    images = []
    with open(file_name, 'r') as f:
        for line in f:
            cols = line.split(',')
            # print(cols)
            labels.append(cols.pop(0))
            values = list(map(lambda n: int(n) / 256, cols))
            images.append(values)
    return {"labels": labels, "images": images}


train_data = load_csv("./mnist/train.csv")

test_data = load_csv("./mnist/t10k.csv")

#
# #알고르짐 선택
clf = svm.SVC()
#
# #학습
clf.fit(train_data['images'], train_data['labels'])
#
# #예측
predict= clf.predict(test_data['images'])
#
# #정확도
ac_score = metrics.accuracy_score(test_data['labels'], predict)
cl_report = metrics.classification_report(test_data['labels'], predict)
print(f"정확도: {ac_score}")
print("리포트=")
print(cl_report)
