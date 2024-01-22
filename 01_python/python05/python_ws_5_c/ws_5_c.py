def restructure_word(word, arr):
    for w in word:
        if w.isdecimal():
            for i in range(int(w)):
                arr.pop()
        else:
            arr.remove(w)
    
    result = arr
    return result


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
for w in original_word:
    arr.append(w)
print(arr)


result = restructure_word(word, arr)
print(result)
print(''.join(result))