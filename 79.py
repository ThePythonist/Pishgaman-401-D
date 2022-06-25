def f(a,b):
    if b == 1 :
        return a
    else :
        return a * f(a,b-1)

print(f(2,3))
