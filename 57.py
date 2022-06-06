nomarat = {
    "hesaban":18,
    "farsi":9,
    "tarikh":14,
    "hendese":16,
    "zaban":20,
}

for i,j in nomarat.items():
    if j > 10 :
        print(i,": Ghabol")
    else :
        print(i,": Rad")

lst = [ i for i in nomarat.values() ]
moadel = sum(lst) / len(nomarat)
print("Moadel :",moadel)
