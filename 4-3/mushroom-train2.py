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
    #버섯의 측징 기호를 리스트로 표현


    #22번 반복하면서 각각의  행으로 분할
    for col_idx, val in enumerate(row.loc[1:]):
        # print(col_idx, end= ' ')
        # print(val, end=' ')
        if row_idx == 0:
            attr = {"dict": {}, "cnt": {}}
            attr_list.append(attr)
        else:
            attr = attr_list[col_idx]
        #버섯의 속성 값, 12개
        d = [0,0,0,0,0,0,0,0,0,0,0,0,0 ]

        #어디에 1 을 찍어 줄 것인가?
        if val in attr["dict"]:
            idx = attr[]
        else:
            id =attr['cnt'] #0 = attr[0] 첫번째 데이터
            attr["dic"][val] = idx#{'x':0} {'s':0} {'n':0}
            attr['cnt'] += 1# idx =하나의 속성에서 문자데이터 종류





    if row_idx > 3:
        break
# print(data[0])
# #학습데이터/테스트 데이터 분할
# train_data, test_data, train_label, test_label = \
# train_test_split(data, label)
# #
# #모델 학습
# clf = RandomForestClassifier()
# clf.fit(train_data,train_label)
# # 예측
# predict = clf.predict(test_data)
#
# #정답 확인
#
# ac_score = metrics.accuracy_score(test_label, predict)
# cl_report = metrics.classification_report(test_label, predict)
# print(f"정답률: {ac_score}")
# print(f"리포트: {cl_report}")