pro_num = 1000

global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}


def increase(num):
    return num + 1

def creata_data(subject, day, title=None):
    data = {
        '과목': subject,
        '일차': day,
        '제목': title,
        '문제 번호': pro_num,
    }
    return data

pro_num = increase(pro_num)
result_1 = creata_data('python', 3)
print(result_1)
pro_num = increase(pro_num)
result_2 = creata_data('web', 1, 'web 연습하기')
print(result_2)
pro_num = increase(pro_num)
result_3 = creata_data(**global_data)
print(result_3)
