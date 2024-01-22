# 아래 함수를 수정하시오.
def even_elements(num_list):
    num_list_lenght = len(num_list)
    result_str = ''
    result = []

    for i in range(num_list_lenght):
        num = num_list.pop(0)
        if num % 2 == 0:
            result_str += str(num) + ' '
    
    result.extend(list(map(int, result_str.split())))
          
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
