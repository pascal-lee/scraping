import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#데이터 읽기
mr = pd.read_csv("mushroom.csv", header=None)

print(mr.head(10))
data = []
label = []

for row_idx, row in mr.iterrows():
    label.append(row.loc[0])
    #print(f" row: {row.loc[0]}")
    #print(f" {row_idx},\t {row}")
    raw_data = []
    for attr in row.loc[1:]:
        raw_data.append(ord(attr))
    data.append(raw_data)
    # if row_idx > 3:
    #     break
# print(data[0])
# #학습데이터/테스트 데이터 분할
train_data, test_data, train_label, test_label = \
train_test_split(data, label)
#
#모델 학습
clf = RandomForestClassifier()
clf.fit(train_data,train_label)
# 예측
predict = clf.predict(test_data)

#정답 확인

ac_score = metrics.accuracy_score(test_label, predict)
cl_report = metrics.classification_report(test_label, predict)
print(f"정답률: {ac_score}")
print(f"리포트: {cl_report}")