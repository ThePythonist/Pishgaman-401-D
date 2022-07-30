class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.width * self.length)

    def perimeter(self):
        print((self.length + self.width) * 2)


shape = Rectangle(10, 20)
shape.area()
