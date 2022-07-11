# lines = open("words.txt","r").readlines()
#
# output = ""
#
# for line in lines :
#     if len(line) == 6 :
#         output += line
#
# open("5-letter.txt","w").write(output)
# print("Done")


lines = open("words.txt","r").readlines()

lst = []

for line in lines :
    if len(line) == 6 :
        lst.append(line)

output = "".join(lst)

open("5-letter.txt","w").write(output)
print("Done")
