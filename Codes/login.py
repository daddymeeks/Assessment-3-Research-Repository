username = input("Enter the username: ")
password = input("Enter the password: ")

users = ["Marina", "Fiona", "Adam"]
passwords = ["0000", "1111", "1234"]

# if (username == "Marina" and password == "0000") or (username == "Fiona" and password == "1111") or (username == "Adam" and password == "1234"):
#     print("Login successful")
# else:
#     print("Password or login is incorrect")
RED = "\033[32m";
GREEN = "\033[31m";
RESET = "\033[0m";


for i in range(len(users)):
    if username == users[i] and password == passwords[i]:
        print(RED + "login successful" + RESET)
        exit();

print(GREEN + "Password or login is incorrect" + RESET);

#Comments

# User Input:
#     The first two lines of code are prompting the user to enter a username and password using the input() function.
#     The input values are then stored in the variables username and password.

# List and Array:
#     The next two lines define two lists, users and passwords, which store the valid usernames and passwords for the program. 
#     Each element in the users list corresponds to the password in the same position in the passwords list. \
#     In this program, the valid usernames are "Marina", "Fiona", and "Adam", and the corresponding passwords are "0000", "1111", and "1234", respectively.

# Iteration and Conditional Statements:
#     The program then uses a for loop to iterate through the users list to check if the entered username and password match any of the valid combinations of usernames and passwords.
#     If a match is found, the loop prints "login successful" using the RED color code to make it visually prominent and exits the program using the exit() function.
#     If no match is found, the loop prints "Password or login is incorrect" using the GREEN color code to make it visually prominent.

# Printing Output:
#     The print() function is used to display the result of the login attempt. 
#     In this program, the RED, GREEN, and RESET color codes are used to change the color of the text displayed in the console. 
#     The RED color code is used to display the "login successful" message, while the GREEN color code is used to display the "Password or login is incorrect" message.

# In summary, this program demonstrates how to use lists and arrays, iteration, conditional statements, and console output in Python to create a simple login system. 
# It prompts the user to enter a username and password, compares the entered values to a list of valid usernames and passwords, 
# and prints a message indicating whether the login attempt was successful or not.