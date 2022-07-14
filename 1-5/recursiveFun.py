from urllib.parse import urljoin

base = "http://example.com/html/a.html"
print(urljoin(base, "sub/c.html"))
print(urljoin(base, "b.html"))
print(urljoin(base, "../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))

def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(5)