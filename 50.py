number = int(input("Enter any number : "))
divs = []

for i in range(1,number+1):
    if number % i == 0 :
        divs.append(i)

prime_status = False

if len(divs) == 2 :
    prime_status = True

print(prime_status)
