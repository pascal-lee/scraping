from bs4 import BeautifulSoup
fp = open("books.html",encoding="utf-8")
soup =BeautifulSoup(fp,"html.parser")

#CSS 선택자
sel = lambda q:print(soup.select_one(q).string)
sel("#nu") # id 선택자
sel("li#nu") #id 속성이 nu인 것 중 li태그 인 것
sel("ul > li#nu")# id 속성이 nu인 것 중 li태그 이면서 ul의 자식 태그
sel("#bible  #nu")# id속성이 bible 아래의 nu 인것
sel("#bible > li#nu")# id 속성이 bible아래의 nu인 것
sel("ul#bible > li#nu")# id속성이 bible인 ul자식 중 id 속성이 nu태그
sel("li[id ='nu']")#  속성 검색으로 id가 nu인 li태그
sel("li:nth-of-type(4)") # 4번째 li 태그 검색

print(soup.select("li")[3].string) # li 태그를 추출하여 3번째 요소부터(0부터)
print(soup.find_all("li")[3].string)