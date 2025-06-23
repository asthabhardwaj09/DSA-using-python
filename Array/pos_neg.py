# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.

# def neg_pos(arr):
#     positive=[]
#     negative=[]
#     for i in arr:
#         if i>0:
#             positive.append(i)
#         elif i<0:
#             negative.append(i)
#     c=positive+negative
#     return c
# print(neg_pos([-12, 11, -13, -5, 6, -7, 5, -3, -6]))

# import random

# def create_random_array(arr):
#     new_arr = arr[:]         # Make a copy of the original array
#     random.shuffle(new_arr)  # Shuffle it randomly
#     return new_arr

# # Example
# original = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# print(create_random_array(original))

import random

def create_random_array(arr):
    new_arr = arr  # No slicing
    random.shuffle(new_arr)
    print(arr)  #we are using : because original array also get suffle prove chahiye to ye line chala ke dekh lo
    return new_arr

original = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(create_random_array(original))



# random is not a reserved word. It is the name of a standard library module used for random number generation and operations like shuffle, randint, etc. But we should avoid using random as a variable name to prevent conflicts."



