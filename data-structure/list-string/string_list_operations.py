'''
Methods for string and list operations
By Binggang Liu
'''

'''
Methods for string operations

A string is typically considered a list, but unlike list, string is immutable.
'''

my_word = 'abcdefg'
my_sentence = "I have a big dog."


''' slicing '''

my_sentence[-1]
# will return '.'

my_word[1:4]
# will return 'bcd', i.e., element index 1 to 3, before 4

my_word[1:]
# will return 'bcdefg', from index 1 to end

my_word[::2]
# will return 'aceg', every 2nd element, including index 0, the beginning character

my_word[::100]
# will return 'a', the beginning character, even 100 is far beyond the index range

my_word[::-1]
# will return 'gfedcba', just the reverse of my_word[::1]

my_word[-6:-3]
# will return 'bcd'

my_word[:4] + '-x-' + my_word[4:]
# will return: 'abcd-x-efg', note that my_word[4:7] = '-x-'  won't work, since strings are immutable

my_word.replace('d', 'y')
# will return: 'abcyefg'. This generates a new string, the original my_word is not changed


''' splitting '''

my_sentence.split(' ')   # will return: ['I', 'have', 'a', 'big', 'dog.']

my_sentence.split('g')   # will return: ['I have a bi', ' do', '.']

new_string = "34:56:67"
new_string.split(':')   # will return: ['34', '56', '67']


'''
methods for list operations
'''

my_list = ['Kate', 'John', 'May', 'Ted']


''' join() '''

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
