import random
# # lists, arrays
# # empty list
# fruits = []; 
# fruits = ["Apple", "Pineapple", "Banana", "Lemon"];
# # display list
# print(fruits);
# # display element of the list
# print(fruits[1])
# print(fruits[0])

# # add elements to list
# fruits.append("Orange")
# fruits.append("Pear")
# fruits.append("Apricot");
# print(fruits)

# # delete the element
# fruits.pop(1)
# print(fruits)

# select all elements one by one
# for fr in fruits:
#     print(fr)

# generate random numbers
numbers = []
for i in range(100):
    numbers.append(random.randint(0, 1000))

print(numbers)

# select all numbers greate than 500
for n in numbers:
    if n > 500:
        print(n)

# find the max number
# max_number = 0;
# for n in numbers:
#     if n > max_number:
#         max_number = n;

max_number = max(numbers);
min_number = min(numbers)


print("max number = ", max_number);
print("min number = ", min_number);

# display elements

#Comments

# Importing a module:
#     The first line of the code imports the random module in Python.    
#     The random module provides a set of functions to generate random numbers in Python.

# Lists and Arrays:
#     The program demonstrates how to create, add, remove, and iterate through lists in Python.
#     The commented-out code at the beginning shows how to create a list of fruits, add and remove elements from the list, and iterate through the elements of the list.

# Generating Random Numbers:
#     The program uses a for loop and the random.randint() function to generate 100 random numbers between 0 and 1000. 
#     The random.randint() function generates a random integer between the two values provided as arguments.

# Iteration and Conditional Statements:
#     The program then uses a for loop to iterate through the list of random numbers and prints any number greater than 500 to the console.

# Finding the Maximum and Minimum Number:
#     The program uses the max() and min() functions to find the maximum and minimum numbers in the list of random numbers.

# Printing Output:
#     The print() function is used to display the result of the program. 
#     The program displays the list of random numbers, any numbers greater than 500, the maximum and minimum numbers in the list.

# In summary, this program demonstrates how to use lists, arrays, iteration, conditional statements, and importing a module in Python to generate and manipulate a list of random numbers. 
#     It generates a list of random numbers, finds the maximum and minimum numbers in the list, 
#     and prints the list, any numbers greater than 500, and the maximum and minimum numbers to the console.