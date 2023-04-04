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