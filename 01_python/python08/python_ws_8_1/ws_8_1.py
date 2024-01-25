class Animal:
    num_of_animal = 0

    @classmethod
    def animal_increase(cls):
        Animal.num_of_animal += 1

class Dog(Animal):
    def __init__(self):
        super().animal_increase()


class Cat(Animal):
    def __init__(self):
        super().animal_increase()

class Pet(Dog, Cat):
    
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
