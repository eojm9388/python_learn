# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    @classmethod
    def animal_increase(cls):
        Animal.num_of_animal += 1

class Cat(Animal):

    def __init__(self, cat_meow):
        self.cat_meow = cat_meow
        
    def meow(self):
        print(self.cat_meow + ' !')


cat1 = Cat("야옹")
cat1.meow()


