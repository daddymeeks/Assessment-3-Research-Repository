# class declaration
class Cat():
    # attributes = properties = fields
    name: None;
    age: None;
    isHappy: None;

    # constructor
    def __init__(self, name, age, isHappy):
        self.name = name;
        self.age = age; 
        self.isHappy = isHappy;

    # method
    def display(self):
        print("***** CAT *****");
        print("name:", self.name);
        print("age: ", self.age);
        print("is Happy? ", self.isHappy)

    def sound(self):
        print("Meow!");

cat1 = Cat("Peter", 5, True);
cat1.display()
cat1.sound()

cat2 = Cat("Luna", 2, False);
cat2.display()
cat2.sound()

#Comments

# The code above is an example of object-oriented programming (OOP) in Python, using a class named Cat that represents a cat object.

# The class contains several components:

# Attributes: name, age, and isHappy are the properties of the Cat class.
# Constructor: __init__() is a special method that is called when an object is created. It initializes the values of the properties with the arguments passed in.
# Methods: display() and sound() are methods that define the behavior of the Cat object. display() displays the properties of the Cat object, and sound() makes the Cat object meow.
# In the main program, two Cat objects (cat1 and cat2) are created, with their respective properties passed in as arguments. 
# Then, the display() and sound() methods are called on each object to display their properties and make them meow.

# This example demonstrates how classes can be used to create objects with specific attributes and behaviors, 
# and how methods can be used to define the actions or operations that an object can perform.