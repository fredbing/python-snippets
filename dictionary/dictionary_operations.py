'''
This is a Python dictionary operation examples
By Binggang Liu

A dictionary is an unordered collection of key-value pairs. Each item inside a dictionary must to be 
a key-value pair. Inside a dictionary , there can be another dictionary or dictionaries which have key-value pairs
enclosed in curly brackets { }. Note that key-value pairs cannot be put into square brackets [ ]or parentheses ( ).

'''
# A dictionary is unordered collection of key-value pairs
my_dictionary = {1: 'key', 2: 'dal', 'name': 'Murphy', 3: [1, 2, 3]}
# print(my_dictionary)

# both keys and values can be totally different types,
# dictionary is mutable and can be modified using assignment operator
my_dictionary = {2: 'ball', 1: 'apple', 'name': 'Murphy', 3: [1, 2, 3], 14: 'pear', 5: '', 6: None,
                 'Daniel': 20, 'Kevin': 40, 'Jake': 40, None: [201, 'Deer', 'SHEEP', '301'], False: [0, 0]}
# print(my_dictionary)


# check the keys in dictioary
print('Kevin' in my_dictionary)  # will return True, since this is a key
print('ball' in my_dictionary)  # will return False, since this is a value


# access elements in dictioary
print(my_dictionary[1], my_dictionary['name'])
print(my_dictionary[3])
print(my_dictionary.get('name'))
print(my_dictionary.get(2))


# print out all keys
for name in my_dictionary:  # or, for name in my_dictionary.keys():
    print(name)

# print out all values only
for value in my_dictionary.values():
    print(value)

# print out all keys and values:
for name in my_dictionary:
    print("{} : {}".format(name, my_dictionary[name]))

# another way to print out all keys and values:
for (key, value) in my_dictionary.items():
    print(key, value)

# add an item to the dictionary
my_dictionary['city'] = 'Corcoran'
# print(my_dictionary)
my_dictionary['Mary'] = 65
my_dictionary[65] = 'Mary'
# print(my_dictionary)

# delete elements
print(my_dictionary.pop(2))  # remove the key-value pair with key = 2
# print(my_dictionary)

# remove the last key-value pair in the dictionary
print(my_dictionary.popitem())
# print(my_dictionary)

del my_dictionary['name']  # remove the key-value pair with key = 'name'
# print(my_dictionary)

my_dictionary.clear()  # remove all items
print(my_dictionary)
