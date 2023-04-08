# DRY

from circle_formulas import *;



r1 = 2;
s1 = circumference(r1)
print(s1);

r2 = 10;
s2 = circumference(r2)
print(s2);

r3 = 112;
s3  = circumference(r3)
print(s3);

#Comments

# Importing a module:
#     The first line of the code imports a module called circle_formulas using the import statement. This module contains various formulas related to circles.

# DRY Principle:
#     The acronym DRY stands for "Don't Repeat Yourself." This principle is used in software development to reduce repetition in code and improve code quality and maintainability. 
#     In this program, the DRY principle is applied by defining a variable r1 with a value of 2, and then calling the circumference() function from the circle_formulas module with r1 as an argument. 
#     The result is then printed to the console. This is repeated for r2 and r3. By doing this, the code avoids repetition and makes it easier to maintain and modify in the future.

# Calling a function:
#     The circumference() function is called with a value of r1, r2, and r3 as arguments. 
#     This function is defined in the circle_formulas module and calculates the circumference of a circle with the radius passed as an argument.

# Printing Output:
#     The print() function is used to display the result of the program. The program displays the circumference of the circles with radii r1, r2, and r3 to the console.

# In summary, this program demonstrates how to apply the DRY principle in Python by using variables and calling functions to avoid repetition in the code. 
# It imports a module called circle_formulas that contains various formulas related to circles, calls the circumference() function with different radii as arguments, and prints the result to the console.