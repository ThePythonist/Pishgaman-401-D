def zarb(x,y):
    if y == 1 :
        return x
    else :
        return x + zarb(x,y-1)

print(zarb(2,3))
