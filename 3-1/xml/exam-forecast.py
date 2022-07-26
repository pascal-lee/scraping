from bs4 import BeautifulSoup
import urllib.request as req
import os.path

#xml dowload
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
savename ="today_forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename,"r",encoding='utf-8').read()
soup = BeautifulSoup(xml,'html.parser')
#print(f"soup:{soup}")
# 현재 습도 스크래핑
cur_humidity=soup.select_one("dd.desc:nth-child(4)").string
print(f"현재습도:{cur_humidity}")
#6시간 후의 날씨 예보
weather_after_six=soup.select_one("div.open > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(7) > dl:nth-child(1) > dd:nth-child(2) > i:nth-child(1) > span:nth-child(1)").string
print(f"6시간 후 날씨:{weather_after_six}")
