numbers = []

for i in range(3):
    x = input("Entry : ")

    try :
        x = float(x)
        numbers.append(x)
    except ValueError :
        print("Meghdar vared shode mored ghabol nist")

print(numbers)
