# 아래 함수를 수정하시오.
def difference_sets(set_1, set_2):
    # result = set_1 - set_2
    # result = set()
    # for num in set_1:
    #     if num not in set_2:
    #         result.add(num)

    result = set_1.difference(set_2)

    return result


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
