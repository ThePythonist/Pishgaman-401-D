# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# b = B()
# b.say_goodbye()
# b.say_hello()

#-------------------------------------------------------

class Pedar:
    def __init__(self, lname, address, eyecolor):
        self.lastname = lname
        self.address = address
        self.eyecolor = eyecolor

    def say_hello(self):
        print("Hello")


class Farzand(Pedar):
    def __init__(self, lname, address, eyecolor, age):
        super().__init__(lname, address, eyecolor)
        self.age = age

    def say_goodbye(self):
        print("Goodbye")


pedar = Pedar("Ahmadi", "Jomhori Street", "Brown")
pesar = Farzand("Ahmadi", "Jomhori Street", "Brown", 14)

print(pesar.lastname)
print(pesar.age)

#-------------------------------------------------------

# class A:
#     def __init__(self,fname="Ahmadi"):
#         self.familyname = fname
#
#
# class B:
#     def __init__(self):
#         self.pedar = A()
#
# pedar = A()
# pesar = B()
#
# print(pesar.pedar.familyname)
