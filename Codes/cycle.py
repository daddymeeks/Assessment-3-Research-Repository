import time;
counter = 5;


# while counter >=0:
#     time.sleep(1);
#     print(counter);
#     counter -= 1; # counter = counter - 1

# timer - while loop
# sec = 0;
# while True:
#     # wait for 1 secons
#     time.sleep(1)
#     sec += 1;
#     print(sec)

# for loop
for sec in range(5, 0, -1):
    time.sleep(1)
    print(sec)

#Comments

# This code demonstrates the use of loops and the time module in Python.

# The code starts by importing the time module. This module provides various time-related functions in Python.

# The next line initializes a variable called "counter" to 5.

# The first loop in the code is a while loop that counts down from 5 to 0. In each iteration of the loop, 
# the code waits for 1 second using the time.sleep() function and then prints the value of the "counter" variable. 
# Finally, the "counter" variable is decremented by 1 using the "-=" operator.

# The second loop in the code is also a timer loop, but it uses a "while True" loop to keep running indefinitely. 
# In each iteration of the loop, the code waits for 1 second using the time.sleep() function and then increments the "sec" variable by 1. 
# The value of "sec" is then printed.

# The third loop in the code is a for loop that counts down from 5 to 1. 
# In each iteration of the loop, the code waits for 1 second using the time.sleep() function and then prints the value of the "sec" variable, which is initialized to 5 and decremented by 1 in each iteration of the loop.

# Overall, this code demonstrates how to use loops and the time module in Python to create timers and countdowns.