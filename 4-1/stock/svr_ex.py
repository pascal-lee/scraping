import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

import numpy as np
import matplotlib.pyplot as plt

# 삼성전자 주식 파일( ss_stock.csv) 불러오기
stock_df1= pd.read_csv("ss_stock.csv")
#주가 데이터 추출
df = stock_df1[['Price']]
#1000개의 데이터만 사용
df = df.iloc[:1000]
print(f"head: {df.head(10)}")

#15일 후 주가를 예측 데이터로 사용
df['Prediction'] = df[['Price']].shift(30)

# 데이터 셋  X 생성
X = np.array(df.drop(['Prediction'],1))
#Remove the last 15 rows
X = X[30:]

print(f'데이터셋 X 확인: {X[:10]}')

# 예측 데이터 셋 Y 정의
# Create a dataset y which will be having Predicted values and convert into numpy array
y = np.array(df['Prediction'])
# Remove Last 15 rows
y = y[30:]
#print(y[:10])

# train data vs. test data split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

#모델 생성 및 훈련

# SVM Model
svr = SVR(kernel='rbf', C=1e3, gamma=0.1)
# Train the model
svr.fit(x_train, y_train)

# 테스트 데이터
forecast = np.array(df.drop(['Prediction'],1))[:30]
print(f'실제값: {forecast}')
# 데이트 예측 결과
svm_prediction = svr.predict(forecast)
print(f'예측값: {svm_prediction}')


