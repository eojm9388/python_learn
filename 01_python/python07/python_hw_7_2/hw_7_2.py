# 아래 클래스를 수정하시오.
class StringRepeater:
    
    def repeat_string(self, count, word):
        for i in range(count):
            print(word)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
