'''
This is a Python tuple operation example
By Binggang Liu

A tuple is like a list but immutable. Tuples use parentheses instead of square brackets.
Common use cases for tuples include colors, e.g., red(255,0,0), purple(255,0,255), 
and geolocations(latitude, longitude)
Though a tuple is immutable, the elements inside a tuple can be mutable if the element itself is mutable, 
for example, if the element is a list.

'''

my_tuple = ('Ab', "Cathy", 'Dave', 'Ethan', 'Frank')
print(my_tuple[0])

for n in my_tuple:
    print("Hello! {}, ".format(n) + " very nice meeting you!")


# Switch from tuple to list or vice versa
my_list = list(my_tuple)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

# Tuple is immutable, but inside the element it can be mutable
new_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
# new_tuple[0] = [11,12,13] #This won't work, since the element is immutable, but inside the element it is mutable
new_tuple[0][0] = 11
new_tuple[0][1] = 12
new_tuple[0][2] = 13
print(new_tuple)
