import requests

#image download
url ="https://www.hanbit.co.kr/data/books/B8068754595_l.jpg"
r = requests.get(url)
with open("test.jpg","wb") as f:
    f.write(r.content)

print("saved")