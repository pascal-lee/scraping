from bs4 import BeautifulSoup
import requests
import re
import re
ticker="005930"
url=f"https://finance.naver.com/item/sise_day.naver?code={ticker}&page=1"
#url = f"https://fchart.stock.naver.com/sise.nhn?symbol={ticker}&timeframe=day&count=3000&requestType=0"
#url =f"https://api.finance.naver.com/siseJson.naver?symbol={ticker}&requestType=2&count=5&startTime=20220719&timeframe=day"
results=requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'})
#print(results.text)
soup = BeautifulSoup(results.text,'html.parser')
# find number of pages
#.pgRR > a:nth-child(1)
#print(soup)
#print(soup.prettify())
#items = soup.find_all("td",{"class":"pgRR"})[0]
#items = soup.select("td.pgRR>a")[0].attrs['href']
items = soup.select("td.pgRR")[0].a['href']
#items_1 = items.find_all("a")
#a_tag=items[0].find({"a":"href"})
#
# print(items_1)
print(items)
print(f"page: {re.split('page=',items)[1]}")
#.type2 > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > span:nth-child(1)
#.type2 > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > span:nth-child(1)
days = soup.select('tr>td:nth-child(1)>span')
for day in days:
    print(day.string)

prices = soup.select('tr>td:nth-child(2)>span')
for price in prices:
    print(price.string)



# print("")


#print(items[0].find({"a":"href"}))
#print(f'html out:{items[0:2]}')
# for item in items:
#     print(item.find_all('a:href'))

#print(str(items[0]).replace("<item data=""></item>",""))
# for item in items:
#     row=item.s

