# Dictionaries
course = {
    "name": "Software Development Fundamentls",
    "duration": "8 weeks"
}

print(course);

# list = [1, 3, 4, 5]
# list[0]

print(course["name"]);
course["fee"] = 1000.00;
course["copyright"] = "Whitecliffe";
# course["name"] = "Course 1";
# course.update({"name": "Course 2"});
course.pop("fee");
# course.clear();
print(course);

# for key, value in course.items():
#     print(key, value);

for key in course:
    print(key, course[key])

# tuples, sets in Python


#Comments

# The code introduces the concept of dictionaries in Python, which is a data structure that stores data in key-value pairs.

# Firstly, the code initializes a dictionary named "course" that contains two key-value pairs - "name" and "duration". 
# These key-value pairs are accessed using square brackets, such as course["name"].

# The code then demonstrates how to add new key-value pairs to a dictionary using the syntax course["fee"] = 1000.00. 
# It also shows how to update the value of an existing key using course["name"] = "Course 1" or course.update({"name": "Course 2"}). 
# Additionally, the code shows how to remove a key-value pair using course.pop("fee") or remove all key-value pairs using course.clear().

# Finally, the code demonstrates how to iterate over the keys or key-value pairs in a dictionary using a for loop 
# and the items() method or by simply iterating over the keys using for key in course.

# Overall, the code provides a basic understanding of how dictionaries work in Python 
# and how to perform common operations such as adding, updating, and removing key-value pairs, as well as iterating over the keys or key-value pairs in a dictionary.