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

