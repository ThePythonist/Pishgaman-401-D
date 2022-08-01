from Mod import Person, a, b, c, power


class Student(Person):
    def __init__(self, fname, lname, age, student_code, major):
        super().__init__(fname, lname, age)

        self.student_code = student_code
        self.major = major


std1 = Student("Pedram", "Fazli", 24, 1232131545, "Computer Engineering")
std2 = Student("Farzad", "Rahimi", 22, 4635654654, "Electrical Engineering")
std3 = Student("Maryam", "Teymori", 31, 9832761545, "Civil Engineering")
std4 = Student("Amirali", "Jafari", 25, 3132131565, "Acting")

print(std1.fname)
