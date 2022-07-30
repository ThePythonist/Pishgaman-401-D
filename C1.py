class Car:
    def __init__(self, n, m, c):
        # print("Hello from init")
        self.name = n
        self.model = m
        self.color = c

    def Break(self):
        print("Break!")

    def Tell_Info(self):
        print("Car name : ", self.name)
        print("Car model : ", self.model)
        print("Car color : ", self.color)


persia = Car("Pars", "1401", "Black")
persia.Tell_Info()

i8 = Car("I8", "2018", "White")
i8.Tell_Info()
