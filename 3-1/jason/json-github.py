import urllib.request as req
import os.path, random
import json

# 1. JSON  데이터 내려 받기
url = "https://api.github.com/repositories"
savename= "rep.json"

if not os.path.exists(url):
    req.urlretrieve(url,savename)

#2. JSON 파일 분석
temp = open(savename, "r",encoding="utf-8").read()
items = json.loads(temp)
#print(items)

# 3. 파일내용 출력
for item in items:
    print(item["name"],end='')
    print("-",end='')
    print(item["owner"]["login"],end='')