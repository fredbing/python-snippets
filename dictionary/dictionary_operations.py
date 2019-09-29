'''
Python dictionary operation examples
A dictionary is an unordered collection of key-value pairs

Author: Binggang Liu
'''
# unordered collection of key-value pairs
my_dictionary = {2: 'ball', 1: 'apple', 14: 'pear'}
print(my_dictionary)

# both keys and values can be totally different types,
# dictionary is mutable and can be modified using assignment operator
my_dictionary = {1: 'key', 2: 'dal', 'name': 'Murphy', 3: [1, 2, 3]}
print(my_dictionary)

# access elements in dictioary
print(my_dictionary[1], my_dictionary['name'])
print(my_dictionary[3])
print(my_dictionary.get('name'))
print(my_dictionary.get(2))

# add an item to the dictionary
my_dictionary['city'] = 'Corcoran'
print(my_dictionary)
my_dictionary['Mary'] = 65
my_dictionary[65] = 'Mary'
print(my_dictionary)

# delete elements
print(my_dictionary.pop(2))  # remove the key-value pair with key = 2
print(my_dictionary)

# remove the last key-value pair in the dictionary
print(my_dictionary.popitem())
print(my_dictionary)

del my_dictionary['name']  # remove the key-value pair with key = 'name'
print(my_dictionary)

my_dictionary.clear()  # remove all items
print(my_dictionary)
