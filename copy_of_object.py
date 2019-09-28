'''
In Python, when "=" operator is used to create a copy of an object, it does not creates a new object,
but only creates a new variable that shares the reference of the original object. See example below:
'''

ori_obj = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
copied_obj = ori_obj

copied_obj[2][2] = 9

print('Original object:', ori_obj)
print('ID of Original object:', id(ori_obj))

print('Copied object:', copied_obj)
print('ID of Copied object:', id(copied_obj))

'''
The output of running above program:

Original object: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Original object: 123456789234567

Copied object: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Copied object: 123456789234567

In the above programme, if any change is made to either objects, the change is visible in both.

In order to keep the original object unchanged and only modify the new object or vice versa, there are two ways to create copies:

    Shallow Copy
    Deep Copy

'''
# Shallow Copy
'''
A shallow copy creates a new object which stores the reference of the original elements.
It doesn't create a copy of nested objects, instead it just copies the reference of nested objects. 
'''
import copy

ori_obj = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
copied_obj = copy.copy(ori_obj)

print("Original object:", ori_obj)
print("Copied object:", copied_obj)

'''
The output of running above program:

Original object: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Copied object: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''

import copy

ori_obj = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
copied_obj = copy.copy(ori_obj)

ori_obj.append([4, 4, 4])

print("Original object:", ori_obj)
print("Copied object:", copied_obj)

'''
The output of running above program:

Original object: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
Copied object: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

'''

import copy

ori_obj = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
copied_obj = copy.copy(ori_obj)

ori_obj[1][1] = 'AA'

print("Original object:", ori_obj)
print("Copied object:", copied_obj)

'''
The output of running above program:

Original object: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
Copied object: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

'''

#Deep Copy
'''
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
It creates independent copy of original object and all its nested objects.

'''

import copy

ori_obj = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
copied_obj = copy.deepcopy(ori_obj)

print("Original object:", ori_obj)
print("Copied object:", copied_obj)

'''
The output of running above program:

Original object: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
Copied object: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

'''

import copy

ori_obj = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
copied_obj = copy.deepcopy(ori_obj)

ori_obj[1][0] = 'BB'

print("Original object:", ori_obj)
print("Copied object:", copied_obj)

'''
The output of running above program:

Original object: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
Copied object: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

'''