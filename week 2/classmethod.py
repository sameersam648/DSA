class Student:
    count = 0

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        Student.count += 1

    def __str__(self):
        return f"Student's name: {self.name}, Rollnumber: {self.roll}"
    
    @classmethod
    def name_string(cls, data):
        name, roll = data.split(",")
        return cls(name.strip(), int(roll))
#even if the user put's the roll as a string this will speprate it still

s1 = Student("sameer", 100)
s2 = Student.name_string("ameer, 101")

print(s1)
print(s2)
print(f"Number of Students : {Student.count}")

#solved it, sted by step, normal oops, str method, @classmethod