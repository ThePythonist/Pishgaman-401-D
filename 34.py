numbers = [1,2,3,4,5]

for i in range(5) :
    n = int(input("Entry : "))
    if 6 <= n <= 10 :
        # numbers += [n]
        numbers.append(n)

print(numbers)
