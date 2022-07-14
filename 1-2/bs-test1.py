from bs4 import BeautifulSoup

html ="""
<html><body>
<h1>스크래핑이란?</h1>
<p>웹페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것 </p>
</body></html>
"""
print(html)
soup= BeautifulSoup(html,'html.parser')
#print(soup)

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling
p3 = p2.next_sibling
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
print("p = " + p3.string)

title = soup.find(id="title")
body = soup.find(id = "body")

print("#title="+title.string)
print("#body="+body.string)