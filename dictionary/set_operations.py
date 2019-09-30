'''
This is a Python set operation example
By Binggang Liu

A set is a collection of unordored unique items, so index does not work for sets.
Like dictionary, sets use curly brackets, but the elements are just indivisual items, not value-pairs.
The indivisual elements in a set can be sets, dictionaries, lists, tuples, etc.

'''

my_set = {'Ab', "Cathy", 'Dave', 'Ethan', 'Frank'}
# print(my_set[0]) #unlike list or tuple, this operation does not work for set, because a set does not have order or index

for n in my_set:
    print("Hello! {}, ".format(n) + " very nice meeting you!")


# Typical operation methods for sets
my_set.pop()  # pop() for set does not mean to only remove the last element
print(my_set)
my_set.remove('Cathy')
print(my_set)
my_set.add('Mary')
print(my_set)

# Switch among set, list, and tuple
my_list = list(my_set)
print(my_list)
my_tuple = tuple(my_set)
print(my_tuple)
new_set1 = set(my_tuple)
new_set2 = set(my_list)
print(new_set1, new_set2)

# frozenset() function takes an iterable object as input and make it immutable.
# A frozenset is same as a set except it is immutable.
my_frozenset = frozenset(my_set)
print(my_frozenset)

Employee = {'name': 'Alice', 'age': '25', 'gender': 'female', 'city': 'Medina'}
# this will only return the keys, NOT the values in the dictionary
val = frozenset(Employee)
print(val)

c = frozenset({3, 4, 5})
d = frozenset({4, 5, 6})
print(c.union(d))  # will return {3,4,5,6}


# union() and add() functions
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))  # will return {1,2,3,4}
# print(a.add(b)) # this won't work, since element is unique in a set
