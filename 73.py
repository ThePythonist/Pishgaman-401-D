def calculator(n1,op,n2):
    def add():
        return n1+n2

    def substract():
        return n1-n2

    def multiply():
        return n1*n2

    def divide():
        return n1/n2

    if op == "+":
        print(add())
    elif op == "-":
        print(substract())
    elif op == "*":
        print(multiply())
    elif op == "/":
        print(divide())


calculator(
    int(input("Number1 : ")),
    input("Operator : "),
    int(input("Number2 : ")),
)
