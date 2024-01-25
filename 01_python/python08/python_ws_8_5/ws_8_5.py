class Dog:
    sound = '멍멍'

class Cat:
    sound = '야옹'

class Pet(Cat, Dog):

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

p1 = Pet()

print(p1)