class Student:
    count = 0

    def __init__(self, name, roll):
        if not Student.is_not_valid(roll):
            return ValueError("invalid roll number, roll should be > 0")
        self.name = name
        self.roll = roll
        Student.count += 1

    def __str__(self):
        return f"Students name: {self.name}, Student's Roll: {self.roll}"
    
    @classmethod
    def name_string(cls,data):
        name,roll = data.split(",")
        return cls(name.strip, int(roll))
    
    @staticmethod
    def is_not_valid(roll):
        return roll > 0
    

s1 = Student("sameer", 100)
s2= Student.name_string("habib, 100")

print(Student.is_not_valid(5))
print(Student.is_not_valid(-5))

print(s1)
print(s2)


#it was easy i was able to do it at once , 