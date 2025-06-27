class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        milo = Dog("Milo", 5)
        nestle = Dog("Nestle", 3)

# instance methods
    def __str__(self):
        print(f"{milo.name} is {milo.age} years old.")
    
