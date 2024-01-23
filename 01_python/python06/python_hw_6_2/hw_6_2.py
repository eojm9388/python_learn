# 아래 함수를 수정하시오.
def remove_duplicates_to_set(num_list):
    result = set()

    for num in num_list:
        result.add(num)

    return result


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
