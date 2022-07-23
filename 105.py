from random import randint

number = randint(0,20)
chance = 5

while chance > 0 :
    guess = int(input("Enter your guess : "))

    if guess == number :
        print("You won!")
        break
    elif guess > number :
        print("Try lower than",guess)
    else :
        print("Try higher than",guess)

    chance -= 1

if chance == 0 :
    print("You lose! The number was :",number)
