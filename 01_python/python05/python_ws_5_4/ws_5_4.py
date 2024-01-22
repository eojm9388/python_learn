# 아래 함수를 수정하시오.
def capitalize_words(words):
    # result = words.title()
    # return result
    word_list = words.split()
    result = []
    for i in range(len(word_list)):
        result.append(word_list[i].capitalize())
    
        
    result = ' '.join(result)
    return result

result = capitalize_words("hello, world!")
print(result)