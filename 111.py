import math


class Circle:
    def __init__(self, r):
        self.radious = r

    def perimeter(self):
        print((self.radious * 2) * math.pi)

    def area(self):
        print((self.radious ** 2) * math.pi)


r = int(input("Enter radious : "))
dayere = Circle(r)

dayere.perimeter()
dayere.area()
