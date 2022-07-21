import requests
import json

#api  key
apikey ="24dbf937b678c5e8f44f3eb0bbfc2ff1"

#날씨를 확인할 도시 지정
cities =['Seoul,KR','Nonsan,KR','Busan,KR','Jeju,KR', 'Miyazaki,JP','San Jose, US']

#api
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
#켈빈 온도를 섭씨 온도로 변환 함수 정의
k2c = lambda k: k - 273.15

#각 도시의 정보 추출

for name in cities:

    #4-1 API의 URL
    url = api.format(city=name, key=apikey)
    # 4-2 데이터 추출
    r = requests.get(url)
    #print(f"url data: {r.text}")
    # 4-3 결과를 JSON형식으로 변환
    data = json.loads(r.text)
    # print output
    #print(f"위도: {data['coord']['lon']}")
    #print(f"경도: {data['coord']['lat']}")
    print("+도시=",data["name"])
    print("| 날씨=",data["weather"][0]["description"])
    print("| 최저 기온=", k2c(data["main"]["temp_min"]))
    print("| 최고 기온=", k2c(data["main"]["temp_max"]))
    print("| 습도=", data["main"]["humidity"])
    print("| 기압=", data["main"]["pressure"])
    print("| 풍향=", data["wind"]["deg"])
    print("| 풍속=", data["wind"]["speed"])


# API URL구성
#API 요청을 보내 데이터 추출

# 결과를  JSON  형식으로 변환

#결과를 출력