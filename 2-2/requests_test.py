import requests

url = "http://api.aoikujira.com/time/get.php"
#Get 방식
r = requests.get(url) #상태정보

# text 형식으로 추출
text = r.text
print(text)

#바이너리 형식ㅇ로 추출
bin = r.content

print(bin)