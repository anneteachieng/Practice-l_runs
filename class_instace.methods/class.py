#creating classes

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

Miles = Dog("Miles", 4, "grey")
Toby = Dog("Toby", 5, "white")


print(f"{Miles.name} is {Miles.age} years old and {Miles.color}")
