# Easy Examples of zip function..
number_list = [1, 2, 3, 4, 5]
str_list = ['one', 'two', 'three']

# No iterables are passed
# This is a zip object (iterable)
result = zip()
print(type(result))

# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_list = list(result)

# Check how you do NOT need it to convert it to a list
# within the for loop to unpack the zip object, but if its
# converted to a list also works..
# Since zip() generates tuples, you can unpack these in the header of a for loop:
for one, two in list(zip(number_list, str_list)):
    print(one, two)

for one, two in zip(number_list, str_list):
    print(one, two)

# ----------- Time----------
import time

# time() function returns the number of seconds passed since epoch.
print('time.time() ->', time.time())

# Testing comit from pyCharm...
