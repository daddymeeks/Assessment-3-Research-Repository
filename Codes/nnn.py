# the program is calculating 
# nnn + nn + n
n = input("Enter any digit")
# print(type(n))

nn = (n + n)
nnn = (n + n + n)
result = int(n) + int(nn) + int(nnn);

print("nnn + nn + n = ", result)
print(nnn + " + " + nn + " + " + n + " = ", result)
print(f"{n} + {nn} + {nnn} = {result}")

#Comments

# User Input:
#     The first line of code is prompting the user to enter any digit using the input() function, 
#     which is a built-in Python function that allows the program to accept user input. 
#     The input is then stored in the variable n.

# String Concatenation:
#     The next two lines of code are concatenating the input digit n with itself to create two-digit and three-digit strings nn and nnn. 
#     This is achieved by adding the string representation of n to itself one or two times, respectively. 
#     For example, if the user inputs the digit 2, then nn will be equal to the string "22" and nnn will be equal to the string "222".

# Type Conversion:
#     The int() function is used to convert the three-digit and two-digit strings nnn and nn to integers so that they can be added to the original digit n 
#     (also converted to an integer) using the + operator.

# Printing Output:
#     Finally, the print() function is used to display the result of the calculation. 
#     The f-string is used to format the output string, where the variables n, nn, nnn, and result are interpolated into the string using the {} syntax.

# In summary, this program demonstrates how to accept user input, concatenate strings, convert data types, and display output in Python.