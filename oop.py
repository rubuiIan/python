'''
OOP Stands for Object Oriented Programming
A calls is a blueprint we use to create objects.
- A class has the following properties:
    1. A constructor - This is the  special method(class function) used to create an object
    2. An attribute - These are variables declared in the scope of the class.
    3. A method - These are functions that are created inside the class as part of the class. We create them by adding a special parameter self, as their firt parameter
    
Initialization: This is the creating  of an object from a class constructor
    
Pillars of OOP
1. Abstraction: This is the hif=ding complex logics implemented for a particular objective in the form of an object
2. Inheritance: A class can retain the properties of another class e.g theit attributes and methods
3. Encapsulation: This is the regulation of access and modification of a class, properties eg attributes and methods
4. Polymorphism: USed to implemnt the nature of another class without inheriting its properties. 
'''
 
#  def is used when creating funtions
 
class Animal:
    def __init__(self, animal_name, food, animal_family, sound, hobby): # Constructor
        self.name = animal_name
        self.food_character = food
        self.family = animal_family
        self.sound = sound
        self.hobby = hobby
        
    def makes_sound(self):
        return self.sound
        
    def get_hobby(self):
        return self.hobby
      
      
animal1 = Animal("Tiger", "Carnivorous", "Mammal", "Roar", "Hunting")
print(animal1.name)
print(animal1.food_character)
print(animal1.family) 

print(animal1.makes_sound())
print(animal1.get_hobby()) 

animal2 = Animal("Chicken", "Omnivorous", "Mammal", "Clacks", "Digging and Gathering")
print(animal2.name)
print(animal2.food_character)
print(animal2.family) 

print(animal2.makes_sound())
print(animal2.get_hobby())       