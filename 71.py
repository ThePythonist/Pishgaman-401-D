def f(lst):
    del lst[3]
    del lst[4]
    return lst
print(f([11,5,6,10,7,4,23,24,0]))
