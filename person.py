class Student():
    # properties/ attributes
    name = ""
    age = 12
    grade = "6th A"
    house = "Sapphire"
    classteacher = "Poonam Ma'am"

    def __init__(self):
        print("Making a new student")

    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print("Please enter your name: ")
        self.name = input()

    def show_details(self):
        print("The details of the student are: ")
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.house)
        print(self.classteacher)

Varnika = Student()
Ruhanika = Student()
Varnika.change_details()
Varnika.show_details()
