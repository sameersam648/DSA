class Student:

    count = 0

    def __init__ (self, name):
        self.name = name
        Student.count += 1

s1 = Student("Sameer")
s1 = Student("Samee")
s1 = Student("ameer")

print(Student.count)