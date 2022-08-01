class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)


x = Student("Parsa", "Farajzadeh", 14)
print(x.age)
x.printname()
