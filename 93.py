lines = open("words.txt").readlines()
lst = []

for line in lines :
    lst.append(line[:-1])

print(lst)
