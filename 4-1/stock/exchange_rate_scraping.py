from bs4 import BeautifulSoup
import requests
import os.path
import re
import pandas as pd

# web page
page=10
url =f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page={page}"
res=requests.get(url, headers={'User-Agent' :
                                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
#print(results.text)
soup = BeautifulSoup(res.text,'html.parser')

#max page
max_page =455
exchange_rate={'Date':[],'Rate':[]}
for p in range(1,max_page+1):
    if p%10 == 0:
        print(f"Page num: {p}")
    url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page={p}"
    res = requests.get(url, headers={'User-Agent':
                                         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
    soup = BeautifulSoup(res.text, 'html.parser')
    days = soup.select("tr> td:nth-child(1)")
    for day in days:
        exchange_rate['Date'].append(day.string)
    rates = soup.select("tr > td:nth-child(2)")
    for rate in rates:
        exchange_rate['Rate'].append(rate.string.replace(',',''))

exchange_df=pd.DataFrame(exchange_rate)
exchange_df.to_csv('exchange_rate.csv')
