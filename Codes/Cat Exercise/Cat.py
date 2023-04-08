# Polymorphism
# Inheritance
# Encapsulation = private, protected

# Parent class
class Cat():
    __name: None;
    age: None;
    isHappy: None;

    # constructor
    def __init__(self, name, age, isHappy):
        self.name = name;
        self.age = age; 
        self.isHappy = isHappy;

    def display(self):
        print("name:", self.name);
        print("age: ", self.age);
        print("is Happy? ", self.isHappy)

    def sound(self):
        print("Meow!");

# Child class 1
class DomesticCat(Cat):
    owner: None;
    
    # constructor
    # super() calls the parent __init__ method
    def __init__(self, owner, name, age, isHappy):
        super().__init__(name, age, isHappy);
        self.owner = owner;
    
    def display(self):
        print("***** DOMESTIC CAT *****");
        super().display()
        print("owner:", self.owner)


# Child class 2
class WildCat(Cat):
    def hunt(self):
        print("I am hunting....");
    
    # the method sound() is owerriten
    def sound(self):
        print("MEOWWWWWW!");
    
    def display(self):
        print("***** WILD CAT *****");
        super().display();

#Comments

# This code demonstrates the concept of Object-Oriented Programming (OOP) in Python, specifically inheritance, encapsulation, and polymorphism.

# The code defines a parent class called Cat that has three attributes - name, age, and isHappy - and three methods - display, sound, and a constructor (__init__). 
# The display method prints the name, age, and isHappy attributes, and the sound method prints "Meow!".

# The code then defines two child classes that inherit from the Cat parent class - DomesticCat and WildCat. 
# The DomesticCat class adds an owner attribute and overrides the display method to print the owner attribute in addition to the parent class attributes. 
# The WildCat class adds a hunt method and overrides the sound method to print "MEOWWWWWW!" instead of "Meow!". 
# The display method of the WildCat class also overrides the parent method and prints "***** WILD CAT *****" before calling the parent class's display method.

# This code demonstrates the polymorphism principle, as the sound method is overridden in the WildCat class, demonstrating how different child classes can implement their own versions of the same method.

# The code also demonstrates inheritance, where the child classes inherit the attributes and methods of the parent class. 
# The DomesticCat and WildCat classes add their own attributes and methods to the ones already defined in the parent class.

# Finally, the code also demonstrates encapsulation by making the name, age, and isHappy attributes private using double underscore (__) before the attribute name. 
# This means that these attributes cannot be accessed or modified from outside the class, ensuring data integrity and security.