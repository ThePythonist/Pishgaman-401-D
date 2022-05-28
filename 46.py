lst1 = [11,15,11,2,4,4,4,16,15,17]
unique = []

for i in lst1 :
    if i not in unique :
        unique.append(i)

print(unique)

#----------------------------------

unique = list(set(lst1))
print(unique)
