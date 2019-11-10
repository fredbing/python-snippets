'''
Besides multiplication and power operations, asterisk can be used for the following:

(1) variable arguments, e.g., *args, **kwargs
(2) repeatedly extending the list-type containers
(3) unpacking the containers

'''
# (1) *args in function definitions in python is used to pass a variable number of arguments to a function.
#  It is used to pass a non-keyworded, variable-length argument list.. 
# With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
# Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, 
# run some higher order functions such as map and filter, etc.

 
# example of *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'World', 'Python', 'is', 'Great')  

'''
Output:

Hello
World
Python
is
Great
'''

# *args with first extra argument 
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'World', 'Python', 'is', 'Great') 

'''
Output:

First argument : Hello
Next argument through *argv : World
Next argument through *argv : Python
Next argument through *argv : is
Next argument through *argv : 
'''


#  **kwargs in function definitions is used to pass a keyworded, variable-length argument list. The reason for using the name kwargs with the double star 
#       is that the double star allows us to pass through keyword arguments (and any number of them).
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it,  
#  that is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.


# 
# **kargs for variable number of keyword arguments 
  
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Apple', mid ='Banana', last='Grape')     

'''
Output:

last == Grape
mid == Banana
first == Apple
'''


# use *args or **kwargs to pass arguments to function :  

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      

args = ("Adam", "Ben", "Cindy") 
myFun(*args)

'''
Output:

arg1: Adam
arg2: Ben
arg3: Cindy

'''
  
kwargs = {"arg1" : "Eve", "arg2" : "Faith", "arg3" : "George"} 
myFun(**kwargs) 

'''
Output:

arg1: Eve
arg2: Faith
arg3: George
'''

# (2) repeatedly extending the list-type containers
#  multiply the list-type container (includes tuple) and an integer number for extending container data by given number times

# make a new list by repeating a list n times
new_list = [0, 1] * 10 

# make a new tuple by repeating a tuplke n times
new_tuple = (0,1) * 30  

# Extending a list with multiplication of list elements
vector_list = [[1, 2, 3]] 
new_list = []
for i, vector in enumerate(vector_list * 3):     
    print("{0} scalar product of vector: {1}".format((i+1), [(i+1) * e for e in vector]))
    new_list.extend([(i+1) * e for e in vector])
    print(new_list)

'''
Output:

# 1 scalar product of vector: [1, 2, 3]
[1, 2, 3]
# 2 scalar product of vector: [2, 4, 6]
[1, 2, 3, 2, 4, 6]
# 3 scalar product of vector: [3, 6, 9]
[1, 2, 3, 2, 4, 6, 3, 6, 9]

'''

# (3) unpacking containers
# the data are in form of a list, tuple or dictionary, and the function take variable arguments

from functools import reduce

primes = [2, 3, 5, 7, 11, 13]

def product(*numbers):
    p = reduce(lambda x, y: x * y, numbers)
    return p 

product(*primes)
# 30030

product(primes)
# [2, 3, 5, 7, 11, 13]


# tuple operation is the same to list, for dictionary, use ** instead of *
headers = {
    'Accept': 'text/plain',
    'Content-Length': 348, 
    'Host': 'http://mingrammer.com' 
}  

def pre_process(**headers): 
    content_length = headers['Content-Length'] 
    print('content length: ', content_length) 
    
    host = headers['Host']
    if 'https' not in host: 
        raise ValueError('You must use SSL for http communication')  
        
pre_process(**headers)
# content length:  348
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 7, in pre_process
# ValueError: You must use SSL for http communication



# unpack list or tuple data to other variables dynamically
numbers = [1, 2, 3, 4, 5, 6]

# The left side of unpacking should be list or tuple, a comma is required after *variable
*a, = numbers
# a = [1, 2, 3, 4, 5, 6]

*a, b = numbers
# a = [1, 2, 3, 4, 5]
# b = 6

a, *b, = numbers
# a = 1 
# b = [2, 3, 4, 5, 6]

a, *b, c = numbers
# a = 1
# b = [2, 3, 4, 5]
# c = 6
