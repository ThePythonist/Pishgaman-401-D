import math

#Aliasing

# def greetings(name):
#     return "Hello " + name
#
# ahvalporsi = greetings
# print(greetings("Parsa"))
# print(ahvalporsi("Parsa"))


# jazr = math.sqrt
# print(jazr(100))
#
# chap = print
# chap("Hello World")

#------------------------------------------------------

def func(name):
    return "Hello " + name

def call_func(function):
    return function("Parsa")

print(call_func(func))
