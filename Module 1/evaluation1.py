class Person:
    total_people = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self, age):
        if self.age >= 18:
            return True
        else:
            False

    def get_total_people(self):
        return self.total_people
    
    def display(self):
        print(f"The name of the person is {self.name} and the age is {self.age}")


class Student(Person):
    def __init__(self, name, age, scores):
        super().__init__(name, age)
        self.scores = scores
        if self.scores == 0:
            self.scores = []

    def average_score(self):
        if self.scores[0] == 0:
            return 0
        return 
    
    def display(self):
        return super().display()

        