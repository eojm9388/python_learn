# 아래 함수를 수정하시오.
def reverse_string(words):
    result = list(words)
    result.reverse()
    result = ''.join(result)
    return result


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
