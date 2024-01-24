# 아래 클래스를 수정하시오.
class Shape:

    def __init__(self, width, height):
        self.w = width
        self.h = height
        

    def print_info(self):
        print(f'Width: {self.w}')
        print(f'Height: {self.h}')
        print(f'Area: {self.w * self.h}')
        print(f'Perimeter: {2 * (self.w + self.h)}')
        



shape1 = Shape(5, 3)
shape1.print_info()
