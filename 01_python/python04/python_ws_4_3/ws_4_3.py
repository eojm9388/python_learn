import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    company = parsed_data['company']['name']
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    user_name = parsed_data['name']

    if float(lat) < 80 and float(lat) > -80 and float(lng) < 80 and float(lng) > -80:
        name = {
            'company': company,
            'lat': lat,
            'lng': lng,
            'name': user_name,
                        }
        dummy_data.append(name)
    
    

print(dummy_data)