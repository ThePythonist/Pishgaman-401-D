class Person:
    def __init__(self, name, age, blood, height):
        self.name = name
        self.age = age
        self.blood = blood
        self.height = height

    def Talk(self):
        print(f"""
Hello my name is {self.name} and
im {self.age} years old and im {self.height} tall
        """)


male = Person("Parsa", 14, "O+", 183)
female = Person("Tara", 19, "O-", 160)

male.Talk()
female.Talk()
