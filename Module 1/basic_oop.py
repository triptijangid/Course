class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_details(self):
        print(f"Student: {self.name}, Grade: {self.grade}")


    def is_passing(self):
        if self.grade>= 40:
            return True
        else:
            return False


s1 = Student("Tripti", 76)
s1.show_details()
print(s1.is_passing())
s2 = Student("Ronak", 10)
s2.show_details()
print(s2.is_passing())
