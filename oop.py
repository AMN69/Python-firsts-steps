# attributes and class keyword 
mylist = [1,2,3]
myset = set()

class Dog():
    # class object attribute, same for any instance
    species = 'mammal'

    def __init__(self, breed, name, spots): # class constructor
        self.breed = breed # attribute, take the argument and assign with self
        self.name = name
        self.spots = spots # boolean
    
    # methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog(breed='Lab', name='Sammy', spots=False)
print(my_dog.bark(10))

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi
    
    def get_circumference(self):
        return self.radius * Circle.pi * 2 # also self.pi can be used instead of Circle.pi but it's better Circle

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)