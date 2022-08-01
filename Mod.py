class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printname(self):
        print(self.fname, self.lname)


a, b, c = 1, 2, 3


def power(n1, n2):
    print(n1 ** n2)
