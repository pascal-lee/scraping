import pandas as pd
from sklearn import svm, metrics
xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

xor_df = pd.DataFrame(xor_data)
print(xor_df)
xor_df.loc[:,0:1]
print(xor_df.iloc[:,0:2])
xor_label = xor_df.loc[0:3,2]
print(xor_label)

clf =svm.SVC()
clf.fit(xor_data,xor_label)
pre = clf.predict(xor_data)
print(f"예측결과:{pre}")
ac_score=metrics.accuracy_score(xor_label, pre)
print(f"정답률 = {ac_score}")