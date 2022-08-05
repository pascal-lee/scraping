from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# ss stock download via scraper via beautifulsoup
ticker="005930" # 삼성전자 주식 티커
page = 1 #첫페이지 값 저장
# 스크패핑 주소
url=f"https://finance.naver.com/item/sise_day.naver?code={ticker}&{page}=1"
# get 방식으로 데이터 얻어옴
res=requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
#print(results.text)

#Beautifulsoup으로  html 데이터 파싱
soup = BeautifulSoup(res.text,'html.parser')
#선택자를 활용하여 페이지 수 추출
items = soup.select("td.pgRR")[0].a['href']
max_page = int(re.split('page=',items)[1])
print(f"page: {max_page}")

#페이지 별로 주식 데이터 스크래핑
ss_stock={'Date':[],'Price':[]} #  dict 형태로 날짜와 주식 데이터 저장
for p in range(1,max_page):
    #주소 생성
    url2 = f"https://finance.naver.com/item/sise_day.naver?code={ticker}&page={p}"
    #get 방식으로 웹데이터 다운로드
    res2 = requests.get(url2, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
    #beautifusoup으로 데이터 파싱
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    #날짜 스크래핑
    days = soup2.select('tr>td:nth-child(1)>span')
    for day in days:
        ss_stock['Date'].append(day.string)
    #가격 스크래핑
    prices = soup2.select('tr>td:nth-child(2)>span')
    for price in prices:
        ss_stock['Price'].append(price.string.replace(",",""))

print(f"ss stock date :{ss_stock['Date']}")
print(f"ss stock prices:{ss_stock['Price']}")

stock_df=pd.DataFrame(ss_stock) # dict자료 형을 판다스로 변경
stock_df.to_csv('ss_stock.csv') #  csv파일로 데이터 저장


