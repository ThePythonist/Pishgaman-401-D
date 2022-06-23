def prime_status(number):
    divisors = [ i for i in range(1,number+1) if number % i == 0 ]
    # if len(divisors) == 2 :
    #     return True
    # else :
    #     return False
    return True if len(divisors) == 2 else False
print(prime_status(int(input("Enter any number : "))))


# def prime_status(number):
#     divisors = [ i for i in range(1,number+1) if number % i == 0 ]
#     print(True) if len(divisors) == 2 else print(False)
# prime_status(int(input("Enter any number : ")))
