info = {
    "name":"sony",
    "nationality":"japan",
    "founder":"akio morita",
    "field":"tech company"
}

key = input("Enter any key to search in dictionary : ")

if key in info.keys() :
    print("Founded :", info[key])
else :
    print("Not found")
