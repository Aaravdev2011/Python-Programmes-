from abc import ABC , abstractclassmethod

# -- Abstract base class ( Parent )


# Animal inherits from ABC - this makes it an abstract class (Abstraction)
class Animal(ABC):

    # Parent constructor - stores attribuites shared by all animals
    def __init__(self , name , habitat):
        self.name = name
        self.habitat = habitat

        # concrete method - all child classes inherit this for free
    def display(self):
            print(f"Name: {self.name} | Habitat: {self.habitat}")

            # Abstract method - every child class MUST implement this @abstractmethod
    def speak(self):
                pass

            # - CHILD CLASS 1
class Dog(Animal):
    def __init__(self , name , habitat, breed):
        super().__init__(name , habitat) # calls animal's constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says : woof! woof!")


    # - CHILD CLASS 2

class Parrot(Animal):

    def __init__(self, name , habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} (Phrase: {self.phrase})!")



  # - CHILD CLASS 3

class Lion(Animal):

    def __init__(self, name , habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: ROARR!")


    # -- CREATE OBJECTS & RUN THE SHOW

dog = Dog("Bruno", "Home", "Labrador")
Parrot = Parrot("Polly" , "Jungle" , "squawk")
Lion = Lion("simba", "Savannah", "Pride Rock")
print("=== Animal Sound Show ===\n")
for animal in [dog, Parrot, Lion]:
        animal.display()
        animal.speak()
        print()