# names = ["bmw","toyota","maserati","mercedes","audi"]
# lengths = [ len(i) for i in names ]
# d = { k:v for (k,v) in zip(names,lengths) }
# print(d)


names = ["bmw","toyota","maserati","mercedes","audi"]
d = { i:len(i) for i in names }
print(d)
