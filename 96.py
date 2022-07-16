file = open("words.txt").readlines()
rev = []

for word in file :
    rev.append(word[::-1])

print(rev)

output = "".join(rev)
open("Reverse.txt","w").write(output)
