food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

# for index in range(len(food_list)):

#     if food_list[index]['이름'] == '토마토':
#         food_list[index]['종류'] = '과일'
#     elif food_list[index]['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f'{food_list[index]["이름"]} 은/는 {food_list[index]["종류"]}(이)다.')

# print(food_list)

menu_num = 0

while menu_num < len(food_list):
    if food_list[menu_num]['이름'] == '토마토':
        food_list[menu_num]['종류'] = '과일'
    elif food_list[menu_num]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{food_list[menu_num]["이름"]} 은/는 {food_list[menu_num]["종류"]}(이)다.')
    menu_num += 1

print(food_list)