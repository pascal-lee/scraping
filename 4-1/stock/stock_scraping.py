from bs4 import BeautifulSoup
import requests
import os.path
import re
import pandas as pd

# ss stock download via scraper via beautifulsoup
# 페이지 수 추출
ticker="005930"
page = 1
url=f"https://finance.naver.com/item/sise_day.naver?code={ticker}&{page}=1"
res=requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
#print(results.text)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.select("td.pgRR")[0].a['href']
max_page = int(re.split('page=',items)[1])
print(f"page: {max_page}")

# 특정 페이지에서 날짜 및 종가 스크래핑 함수
page = 10
url2 = f"https://finance.naver.com/item/sise_day.naver?code={ticker}&page={page}"
res2=requests.get(url2, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
soup2 = BeautifulSoup(res2.text,'html.parser')
days = soup2.select('tr>td:nth-child(1)>span')
data = soup2.select('tr>td:nth-child(1)>span,tr>td:nth-child(2)>span')
prices = soup2.select('tr>td:nth-child(2)>span')
# for d in data:
#     print(f"data: {d.string}")
# print(f"data list {data}")
#
# for day in days:
#     print(day.string)
# prices = soup2.select('tr>td:nth-child(2)>span')
# print(f"prices  list {len(prices )}")
# for price in prices:
#     print(price.string)

ss_stock={'Date':[],'Price':[]}
for p in range(1,max_page):
    url2 = f"https://finance.naver.com/item/sise_day.naver?code={ticker}&page={p}"
    res2 = requests.get(url2, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    days = soup2.select('tr>td:nth-child(1)>span')
    prices = soup2.select('tr>td:nth-child(2)>span')
    for day in days:
        ss_stock['Date'].append(day.string)
    for price in prices:
        ss_stock['Price'].append(price.string.replace(",",""))

print(f"ss stock date :{ss_stock['Date']}")
print(f"ss stock prices:{ss_stock['Price']}")
stock_df=pd.DataFrame(ss_stock)
stock_df.to_csv('ss_stock.csv')

#환율 스크래핑 날짜, 환율

#한국 은행 이자율: 날짜, 이자율


# FED 이자율 스래핑 날짜, 이자율

