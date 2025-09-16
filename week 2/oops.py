class Students:
    count = 0
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def print_student(self):
        print(f"Student's name : {self.name}, Student's Roll Number : {self.roll_number}")

        Students.count += 1


s1 = Students("Sameer", 100)
s2 = Students("Nasreen", 101)

s1.print_student()
s2.print_student()

print(Students.count)

# okay, i got many things cleared 
# __init__ is a constructor
#self is used to reffer the current object in the class so it is used everywhere

#streak check
#add the count function to this also 