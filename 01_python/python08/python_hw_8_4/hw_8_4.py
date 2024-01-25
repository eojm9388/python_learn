# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):

        print('이름을 입력하세요 : ', end='')
        self.name = input()
        self.user_data['name'] = self.name
        try:
            print('나이를 입력하세요 : ', end='')
            self.age = int(input())
            self.user_data['age'] = self.age
        except ValueError:
            self.user_data['age'] = False
            print('나이는 숫자로 입력해야 합니다.')
            
        
        


    def display_user_info(self):
        if self.user_data.get('name') == '' or not self.user_data.get('age'):
            print('사용자 정보가 입력되지 않았습니다.')
        else:
            print(f'이름: {self.user_data.get("name")}')
            print(f'나이: {self.user_data.get("age")}')



user = UserInfo()
user.get_user_info()
user.display_user_info()
