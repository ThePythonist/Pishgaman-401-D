from random import choice, randint


# def generate():
#     password = []
#     for i in range(6):
#         # x = randint(0,10)
#         x = choice(range(0,10))
#         password.append(str(x))
#
#     output = "".join(password)
#     return output
#
# print("Password : ")
# print(generate())


def generate():
    password = ""
    for i in range(6):
        x = str(randint(0,9))
        password += x
    return password


print(generate())
