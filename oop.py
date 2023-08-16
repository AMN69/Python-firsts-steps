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

# inheritance

class Animal ():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def who_am_i(self):
        print("I am a dog!")
    def eat(self):
        print("I am a dog and eating")
    def bark(self):
        print("WOOF!")

mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()

# polymorphism

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

print("---------")
for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print("---------")
pet_speak(niko)
pet_speak(felix)

class Animal():

    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
print("------------------")
# myanimal = Animal('fred')
# myanimal.speak()

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())

# special methods (Magic/Dunder)

print("---------------")
print("Special methods (Magic/Dunder)")

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # special method to print a class (test it w/o the special method)
        return f"{self.title} by {self.author}"
    def __len__(self): # special method to print the len of the book (test it w/o the special method)
        return self.pages
    def __del__(self):
        print("A book object has been deleted")

b = Book("Python rocks", "Jose", 200)
print(b)
print(str(b))
print(len(b))
del b
print(b) # b doesn't exist anymore, has been deleted but using __del__ special method
