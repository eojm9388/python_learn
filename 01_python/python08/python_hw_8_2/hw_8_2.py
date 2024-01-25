# 아래 함수를 수정하시오.
def check_number():

    while True:
        print('숫자를 입력하세요 : ',end='')
        
        try:
            num = int(input())

            if num > 0:
                print('양수입니다.')
            elif num < 0:
                print('음수입니다.')
            else:
                print('0입니다.')
        except ValueError:
            print('잘못된 입력입니다.')
            break



check_number()
