'''
underscore '-' in Python
(1) storing the result of execution of the previous expression in interpreter (in the interactive shell)
(2) ignoring values
(3) used as a normal variable, such as in looping
(4) separating numbers to make it easy for human reading and understanding
(5) for naming

'''
# (1) Storing the result of execution of the previous expression in interpreter (in the interactive shell)
#  Python automatically stores the value of the last expression in the interpreter to the particular variable  "_" ,
#  the value stored in variable  "_" can be assigned to another variable.


>>> 3*7
21
>>> _     # store result of the previous expressionoperation
21
>>> _ + 7
28
>>> _
28
>>> x = _  # assign value of _ to another variable
>>> x
28



# (2) Ignoring values
# Ignoring means assigning the values to special variable underscore(_). Assigning a value to underscore(_) which is not to be used in future.
# If you don't want to use a specific value while unpacking, just assign that value to underscore(_).

a, _, b = (1, 2, 3)
print(a, b)
'''
results after execution:

1 3
'''

## multiple values can also be ignored 
## use  *(variable)  to assign multiple values to a variable as list while unpacking
## This is called "Extended Unpacking", only available in Python 3.x

a, *_, b = (7, 6, 5, 4, 3, 2, 1)
print(a, b)

'''
results after execution:

7 1
'''

# (3) Used underscore as a normal variable, such as in looping

# lopping 5 times using '_'
for _ in range(5):
    print(_)

# iterating over a list using '_'
scripts = ["Python", "JS", "Bash"]
for _ in languages:
    print(_)

_ = 5
while _ < 10:
    print(_, end = ' ') # default value of 'end' id '\n' in python, here space ' ' is used instead
    _ += 1

'''
results after execution of above code
0
1
2
3
4
Python
JS
Bash
5 6 7 8 9
'''

# (4) Separating numbers to make it easy for reading and understanding
# separate the group of digits, and for different number systems
# you can also check whether they are correct or not by coverting them into integer using "int" method
a_big_number = 26_000_000
binary_number = 0b_0010
octa_number = 0o_64
hexa_number = 0x_23_ab

print(a_big_number)
print(binary_number)
print(octa_number)
print(hexa_number)

'''
results after execution:

26000000
2
52
9131
'''


# (5) For naming

'''
Underscore(_) can be used to name variables, functions and classes, etc..,

    a. Single Leading Underscore: _variable

    b. Signle Trailing Underscore: variable_

    c. Double Leading Underscores:- __variable

    d. Double Leading and Trailing Underscores:- __variable__
'''

# (5)-a: Single Leading Underscore
#  generally for internal use
#  for single leading underscore variables, from M import *  does not import objects whose name starts with an underscore,
#   instead, to import the module normally, e.g., import M

# single leading underscore variable
class InternalVar:

    def __init__(self):
        self.name = "mypydata"
        self._num = 20

obj = internalVar()
print(obj.name)
print(obj._num)

'''
mypydata
20
'''

# single leading underscore function (filename for this code: my_functions.py)

def func():
    return "mypydata"

def _private_func():
    return 20


>>> from my_functions import *
>>> func()
'mypydata'

>>> _private_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_private_func' is not defined


# import the module normally can avoid above error, e.g., import my_functions
>>> import my_functions
>>> my_functions.func()
'mypydata'
>>> my_functions._private_func()
20


# (5)-b: Single Trailing Underscore 
# typical reasons for using Single Trailing Underscore is to avoid conflicts with the Python Keywords 
#  by adding an underscore at the end of the name which you want to use

>>> def function(class):
  File "<stdin>", line 1
    def function(class):
                 ^
SyntaxError: invalid syntax
>>> def function(class_):
...     pass
...
>>>

# (5)-c: Double Leading Underscore 
# used for the name mangling:  tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
dir(obj1)

['_Sample__c',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_b',
 'a']


 class SecondClass(Sample):

    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"
obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
print(obj2.__c)

'''
overridden
overridden


---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-2-4bf6884fbd34> in <module>()
      9 print(obj2.a)
     10 print(obj2._b)
---> 11 print(obj2.__c)


AttributeError: 'SecondClass' object has no attribute '__c'
'''

print(obj2._SecondClass__c)
'''
overridden
'''
print(obj1._Sample__c)

'''
3
'''

# You can access the Double Leading Underscore variables using methods in the class

class SimpleClass:

    def __init__(self):
        self.__mypydata = "This is my Python code"

    def get_datacamp(self):
        return self.__mypydata

obj = SimpleClass()
print(obj.get_mypydata()) # it prints the "This is my Python code" which is a __var
print(obj.__mypydata)     # here, we get an error as mentioned before. It changes the name of the variable
'''
This is my Python code

---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-5-8006c0a9b061> in <module>()
      9 obj = SimpleClass()
     10 print(obj.get_mypydata()) # it prints the "This is my Python code" which is a __var
---> 11 print(obj.__mypydata)     # here, we get an error as mentioned before. It changes the name of the variable


AttributeError: 'SimpleClass' object has no attribute '__mypydata'
'''


# Double Leading Underscore can also be used for the method names

class SimpleClass:

    def __mypydata(self):
        return "mypydata"

    def call_mypydata(self):
        return self.__mypydata()

obj = SimpleClass()
print(obj.call_mypydata()) ## same as above it returns the Dobule pre underscore method
print(obj.__mypydata())    ## we get an error here

'''
mypydata

---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-1-cd8ce2e83589> in <module>()
      9 obj = SimpleClass()
     10 print(obj.call_mypydata()) # same as above it returns the Dobule pre underscore method
---> 11 print(obj.__mypydata())    # we get an error here


AttributeError: 'SimpleClass' object has no attribute '__mypydata'
'''

# Now look at the name mangling in another way. First, create a variable with name _SimpleClass__name, and then try to access that variable using Doble Leading Underscore name.

SimpleClass__name = "mypydata"

class SimpleClass:

    def return_name(self):
        return __name

obj = SimpleClass()
print(obj.return_name()) ## it prints the __name variable

'''
mypydata
'''

#  (5)-d: Double Leading and Trailing Underscores
#  These are called as magic methods or dunder methods
#  it will lead to the clashes if you use these methods as your variable names. So, it's better to stay away from them

class Sample():

    def __init__(self):
        self.__num__ = 20

obj = Sample()
obj.__num__

'''
20
'''
