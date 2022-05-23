# numbers = []
#
# for i in range(5):
#     x = float(input("Enter any number : "))
#     numbers.append(x)
#
# numbers.sort()
# print(numbers[-1])

#---------------------------------------------------

# numbers = list()
#
# for i in range(5):
#     x = float(input("Enter any number : "))
#     numbers.append(x)
#
# maximum = 0
# for n in numbers :
#     if n > maximum :
#         maximum = n
#
# print("Max is : ",maximum)

#---------------------------------------------------

numbers = list()

for i in range(5):
    x = float(input("Enter any number : "))
    numbers.append(x)

print(max(numbers))
