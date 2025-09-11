class Student:
    count = 0

    def __init__ (self, name):
        self.name = name
        Student.count += 1

    def __str__(self):
        return "Students: " + self.name
    
s1 = Student("sameer")
s2 = Student("Ameer")

print(s1)
print(s2)

print(f"No.of Students : {Student.count}")


#more hands on with the class operators and objects of oops
