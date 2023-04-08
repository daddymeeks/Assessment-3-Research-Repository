from Cat import *;
# main process
if __name__ == "__main__":
 
    # instance of child class
    cat1 = DomesticCat("Jane","Peter", 5, True);
    cat1.display()
    cat1.sound()

    # instance of child class
    cat2 = WildCat("Luna", 2, False);
    cat2.display()
    cat2.sound()
    cat2.hunt()

#Comments

# The code above demonstrates the use of object-oriented programming concepts in Python, specifically inheritance and polymorphism.

# The first line imports the Cat module, which contains the Cat, DomesticCat, and WildCat classes defined in the previous code snippets.

# The next lines of code create instances of DomesticCat and WildCat classes, passing in appropriate arguments to their constructors.

# The display() and sound() methods of each class are called on their respective instances, showing how polymorphism works. 
# The display() method is also overridden in the child classes to display additional information.

# Finally, the hunt() method is called on the WildCat instance, demonstrating how the child class can have additional methods specific to its needs.

# The if __name__ == "__main__": block is a common pattern used in Python to prevent code from being executed when the module is imported as a library. 
# In this case, it ensures that the code inside the block is only executed when the file is run as the main program.