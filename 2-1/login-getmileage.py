import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#1.아이디,비밀번호 지정
login_info={'m_id':'bseokl22',
            'm_passwd':'pascal!2357'}
#2.세션시작

session = requests.session()
#3.로그인수행

url_login="https://www.hanbit.co.kr/member/login_proc.php"
res=session.post(url_login,data=login_info)
res.raise_for_status() #오류가 있으면 예외발생
#4.마이페이지 접근
url = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url) #GET 방식
res.raise_for_status()

#print(res)
print(res.text)
#5.마일리지와 이코인
soup=BeautifulSoup(res.text,'html.parser')
mileage=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").text
print(f"마일리지: {mileage}")
# coin
ecoin =mileage=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").text
#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span
print(f"이코인: {ecoin}")