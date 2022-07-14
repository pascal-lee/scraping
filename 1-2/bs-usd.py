from bs4 import BeautifulSoup
import urllib.request as req

#HTML 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

#MTML 분석하기
soup = BeautifulSoup(res,'html.parser')
#원하는 데이터 추출하기
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string
print("usd/krw=",price)
#Gas & Oil price
oil_price = soup.select_one("#oilGoldList > li.on > a.head.wti > div > span.value").string
print("gas/oil=",oil_price)

#gold
#gold_price = soup.select_one("#content > div:nth-child(4) > table > tbody > tr:nth-child(2) > td:nth-child(3)").string
#print("gas/oil=",gold_price)
#kopspi
#kospi_indics = soup.select_one("#KOSPI_now").string
#print("gold=",kospi_indics )

#exchange
exchang1 = soup.select_one("#worldExchangeList > li.on > a.head.jpy_usd > div > span.value").string
print("exchange=",exchang1)