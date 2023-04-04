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