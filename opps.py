class student:
    grade = 10
    print("Hi I am a student of grade", grade)

ob = student()


class student1:
    grade = 10
    name= "PEnguin"

    def introduction(self) :
        print("Hi I am a student")

    def details(self):
            print("My name is", self.name)
            print("I study in grade", self.grade)

ob = student1()
ob.introduction()
ob.details() 




class Parrot:

     # class attribute
     species = "bird"

     # instance attribute
     def __init__(self, name, age):
          self.name = name
          self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old".format (blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))