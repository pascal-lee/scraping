from sklearn import svm
xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

data = []
label = []
for row in xor_data:
    #print(row)
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

print(data)

# train data
clf = svm.SVC()
clf.fit(data,label)
# predict
pre = clf.predict(data)
print("예측결과:",pre)

#confirm expected resuts
ok = 0;total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1
print("정답률:", ok, "/",total, "=",ok/total)
