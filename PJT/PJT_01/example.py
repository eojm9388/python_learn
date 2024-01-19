# 서버로부터 데이터를 가져와보자
# 데이터를 가져오는 python 라이브러리: requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지 이름>
    # 목록 확인 : pip list

# 패키지 추가
import requests 
import pprint   # 출력값이 정리되서 나옴

API_key = 'API_key'
lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(url).json()

# print(data)
pprint.pprint(data['weather'][0]['description'])

