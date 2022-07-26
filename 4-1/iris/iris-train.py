from sklearn import svm, metrics
import random, re

csv = []
with open('iris.csv', 'r',encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        #print(line)
        cols = line.split(',')
        #print(cols)
        # #string to number
        fn = lambda n:float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        #print(cols)
        csv.append(cols)
# removal header\
del csv[0]
# 데이터 셔플(섞기)
random.shuffle(csv)

# 학습데이터아 테스트 데이터 분할(2:1)
total_len = len(csv)
train_len = int(total_len*2/3)
test_len = int(total_len/3)

train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data = csv[i][0:3]
    label = csv[i][4]

    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

#데이터를 학습 시키고 예측하기
#print(f"train_data: {train_data}")
#print(f"train_label: {train_label}")

clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

# accuracy
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률: {ac_score}")


# clf = svm.SVC()
# clf.fit("training data", "labels")
# pre=clf.predict("test data")
#
# ac_score = metrics.accuracy_score('traing labes', 'predicte labels')
# print(f"정답률: {ac_score}")
