# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    @classmethod
    def animal_increase(cls):
        Animal.num_of_animal += 1

class Dog(Animal):
    def __init__(self):
        super().animal_increase()

    def bark(self):
        print('멍멍 !')


class Cat(Animal):
    def __init__(self):
        super().animal_increase()

    def meow(self):
        print('야옹 !')

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def play(self):
        print('애완동물과 놀기')
        
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'



pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
