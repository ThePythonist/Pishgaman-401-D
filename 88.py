lines = open("words.txt","r").readlines()

lst = list()

for line in lines :
    if len(line) == 6 :
        lst.append(line)

print(lst)
