'''
Methods for list operations
By Binggang Liu
'''

'''
list is a collection that is ordered and mutable. It allows duplicate members and different data types.
list can be created in two ways:
(1) using list() constructor; (2) using square bracket [ ]

'''

names = list(("Ab", "Cathy", "Mary", "Peggy"))

my_list = ['Kate', 'John', 'May', 'Ted']


'''
list methods:

append()    my_list.append("David")
clear()     my_list.clear()
copy()      my_list.copy()
count()
extend()
del()       del my_list[0]     del my_list
index()
insert()    my_list.insert(2, 'Ethan')  # insert 'Ethan' at index 2
len()
list()      my_list_copy = list(my_list)
pop()       my_list.pop()     my_list.pop(2)  #this will pop out the element with index 2
remove()    my_list.remove("Ted")
reverse()   my_list.reverse()    # does not return a list (or an object), it just modifys the original list
reversed()  reversed(my_list)    # does not return a list but returns an object, to get the reversed list: list(reversed(my_list))
sort()      my_list.sort()       # does not return a list (or an object), it just modifys the original list
sorted()    sorted(my_list)      # returns an iterable list, can be assigned to a list with different name

'''

''' join() and split() '''

'.'.join(my_list)
# will return: 'Kate.John.May.Ted'

'.'.join(my_list).split('.')
# split again will get the same list


''' append() and pop()'''
my_list.append('Mike')
# will add 'Mike' to end of list

my_list.pop()
# pop() for list will return the last object in the list, here it will return 'Mike'

''' 
extend() v.s. append()
like append(), extend() mutates the original list, and both methods take only 1 argumant. 
The differences are:  extend() extends the original list by appending elements from the iterable, 
while append() will add the entire list as one object and add to the end of the original list
'''
my_list = ['Kate', 'John', 'May', 'Ted']
list2 = [2, 3, 4]

my_list.append(list2)
# will return ['Kate', 'John', 'May', 'Ted', [2, 3, 4]]

my_list.extend(list2)
# if use extend() instead, it will return: ['Kate', 'John', 'May', 'Ted', 2, 3, 4]

list2.append(5)
list2.extend([5])
# also note that the above two operations will give the same end results: [2, 3, 4, 5],
# append(object) can take an integer as input, while extend(list) needs to take a list as input
# list2.extend([5]) is equivalent to  list2 + [5]

list2.extend('uvw')
# when the argumant for extend() is a string, it will entend the original list by adding each of the characters
# into the list: [2, 3, 4, 5, 'u', 'v', 'w']

''' 
remove() v.s. del() v.s. clear()
remove() removes elements by value, e.g., mylist.remove(element)
del() deletes elements by index, e.g., del mylist[index]. It can also delete the entire list, e.g., del mylist, this will totally remove the list
clear() clears the list and make it an empty list
'''
