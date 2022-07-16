import random

while True : 

    x,y = int(input("Enter range start : ")),int(input("Enter range end : "))

    n = random.choice(range(x,y))

    print(n)
