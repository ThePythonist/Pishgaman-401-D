lines = open("words.txt").readlines()

lst = []

for line in lines :
    lst.append(line[0:-1])

output = "".join(lst)

open("1-line.txt","w").write(output)
