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
    


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        company = user['company']
        name = user['name']
        if censorship(company, name):
            censored_user_list[company] = [name]

    
    return censored_user_list  

def censorship(company, name):
    if company in black_list:
        print(f'{company}소속의 {name}은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user(dummy_data))