"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list.
"""

def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    
    while first <= last:
        middle = (first + last) // 2

        if input_array[middle] == value:
            return input_array.index(value) #Is Found, so we return the index of the value in the array.
        else:
            if value < input_array[middle]:
                last = middle - 1 # If Value is smaller, it should be in the first half of the array.
            else:
                first = middle + 1 ## If Value is bigger, it should be in the second half of the array.

    return -1 #Not found.

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)