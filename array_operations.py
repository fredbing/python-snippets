'''
Arrays can hold homogeneous data types
Operating on arrays can be more efficiently while using less memory

'''

from array import array

# create an array of interger type
array1 = array('i', [3,5,7,9,11])
print(array1.typecode)
print("array1 item size: ", array1.itemsize)

# add additional items to the array
array1.insert(0, 1)  # add interger 1 at index 0
array1.append(13)
array1.extend([15,17,19])

# iterate over the array like a list
for i, item in enumerate(array1):
    array1[i] = item * 2
print(array1)


# create an array of byte type (can hold up to 255)
array2 = array('B', [3,5,7,9,11])
print(array2.typecode)
print("array2 item size: ", array2.itemsize)
# array2.append(256) # gives error: OverflowError: unsigned byte integer is greater than maximum

# convert an array to a list
print(array2) # array('B', [3, 5, 7, 9, 11])
list2 = array2.tolist()
print(list2) # [3, 5, 7, 9, 11]