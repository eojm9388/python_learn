# 아래 함수를 수정하시오.
def count_character(words, word):
    result = words.count(word)
    return result
    


result = count_character("Hello, World!", "o")
print(result)  # 2
