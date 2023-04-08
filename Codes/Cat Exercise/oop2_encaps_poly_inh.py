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

# instance of child class
cat1 = DomesticCat("Jane","Peter", 5, True);
cat1.display()
cat1.sound()

# instance of child class
cat2 = WildCat("Luna", 2, False);
cat2.display()
cat2.sound()
cat2.hunt()

# print(cat2.__name)


#Comments

# Inheritance: 
#     The child classes (DomesticCat and WildCat) inherit from the parent class (Cat). 
#     This means that the child classes inherit the attributes and methods of the parent class and can also add their own unique attributes and methods.

# Polymorphism: 
#     The child classes (DomesticCat and WildCat) have overridden the display and sound methods of the parent class (Cat). 
#     This means that the child classes have implemented their own versions of these methods, which are used when these methods are called on instances of the child classes.

# Encapsulation: 
#     The parent class (Cat) has encapsulated the attributes __name, age, and isHappy. 
#     These attributes are only accessible from within the class (i.e., they are private), and cannot be accessed directly from outside the class.

# Constructor: 
#     Each class has a constructor, which is called when an instance of the class is created. 
#     The constructor initializes the attributes of the class with the values passed as arguments to the constructor.

# Super() function: 
#     The super() function is used in the constructors of the child classes to call the constructor of the parent class. 
#     This is necessary in order to properly initialize the attributes of the parent class.

# Method overriding: 
#     The child classes (DomesticCat and WildCat) have overridden the sound method of the parent class (Cat). 
#     This means that the child classes have implemented their own versions of this method, which are used when this method is called on instances of the child classes.

# Polymorphism: 
#     The child classes (DomesticCat and WildCat) have implemented their own version of the display method of the parent class (Cat). 
#     This means that the child classes have implemented their own version of this method, which is used when this method is called on instances of the child classes.

# Overall, this code uses object-oriented programming principles such as inheritance, encapsulation, 
# and polymorphism to create a hierarchy of classes that represent different types of cats with their own unique attributes and methods.