from bs4 import BeautifulSoup

#분석대상 HTML
html = """

<html>
    <body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class ="items art it book">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작한는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body>
</html>
"""
#HTML 분석하기
soup  =BeautifulSoup(html, "html.parser")
##meigen > h1:nth-child(1)
#타이틀(제목) 부분 추출하기
h1 = soup.select_one("div#meigen>h1").string
print("h1=",h1)
##meigen > h1:nth-child(1)

li_list = soup.select("div#meigen > ul>li")
for li in li_list:
    print("li=",li)

