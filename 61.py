string = "Python"
d = {}

for i in range(len(string)):
    d.setdefault(i,string[i])

print(d)
