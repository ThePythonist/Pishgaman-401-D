entry = input("Enter any text : ")

output = f"<h1> {entry} </h1>"

f = open("Template.html", "w").write(output)
print("Done")
