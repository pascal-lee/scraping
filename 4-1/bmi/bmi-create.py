#CSV 파일에 무작위로 키와 몸무게를  생성해서 저장
import random

# bmi를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h,w):
    bmi = w/(h/100) **2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"

# 출력 파일 준비하기
fp = open("bmi.csv","w",encoding='utf-8')
fp.write("height,weight,label\r\n")
# 무작위로 데이터 생성하기
cnt = {"thin":0, "normal":0, "fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(50, 95)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))

# file close
fp.close()
print(f"ok: {cnt}")
