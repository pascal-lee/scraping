from bs4 import BeautifulSoup

html ="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""
#print(html)
#HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

#find_all() 메서드로 추출하기
links = soup.find_all("a")
print(type(links))
#링크 목록 출력
for a  in links:
    #print(a.attrs) #속성 값을 딕셔너리로 출력
    href=a.attrs['href']
    text = a.string # <a>링크 안의 문자열
    print(text, ">",href)

