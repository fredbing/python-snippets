'''
Python Decorator concept illustration step by step, including snippets for:
inner/outer functions
closure
wrapper

'''

from functools import wraps
import time


'''
# Outer and inner functions
def f_outer():
    message = 'Look! This is an outer message. '

    def f_inner():
        print(message)
        print("This message is from inner! ")
    return f_inner()

f_outer()
'''

'''
# Closure
# Returning inner function without parenthesis(), when naming a function using outer function object,
# use parenthesis after the newly named function (e.g., my_func() in snippet below), it will then make 
# the inner function callable(executed). This is known as Closure.
def f_outer():
    message = 'Look! This is an outer message. '

    def f_inner():
        print(message)
    return f_inner

my_func = f_outer()
my_func()
'''

'''
def f_outer(msg):
    message = msg

    def f_inner():
        print(message)
    return f_inner

hello_func = f_outer('Hello')
bye_func = f_outer('Good-bye')

hello_func()
bye_func()
'''


'''
def f_outer(msg):
    def f_inner():
        print(msg)
    return f_inner

hello_func = f_outer('Hello')
bye_func = f_outer('Good-bye')

hello_func()
bye_func()
'''


'''
# wrapper in decorator just like a closure
def decorator_func(ori_func):
    def wrapper_func():
        print('wrapper func executed before the {} function'.format(ori_func.__name__))
        return ori_func()
    return wrapper_func


def display():
    print('display function executed')


decorated_display = decorator_func(display)

decorated_display()
'''

'''
def decorator_func(ori_func):
    def wrapper_func():
        print('wrapper func executed before the {} function'.format(ori_func.__name__))
        return ori_func()
    return wrapper_func


@decorator_func
def display():
    print('display function executed')


display()
'''

'''
def decorator_func(ori_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper func executed before the {} function'.format(ori_func.__name__))
        return ori_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def display_multi_args(name, gender, age):
    print('display_multi_args function executed with multiple args ({}, {}, {})'.format(
        name, gender, age))


display_multi_args('Mary', 'F', 36)
'''
'''
# use decorator class instead of decorator function


class Decorator_Class(object):
    def __init__(self, ori_func):
        self.ori_func = ori_func

    def __call__(self, *args, **kwargs):
        print('call method executed before {} function'.format(
            self.ori_func.__name__))
        return self.ori_func(*args, **kwargs)


@Decorator_Class
def display_multi_args(name, gender, age):
    print('display_multi_args function executed with multiple args ({}, {}, {})'.format(
        name, gender, age))


display_multi_args('Mary', 'F', 36)
'''

# create a decorator function: my_logger


def my_logger(ori_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        ori_func.__name__), level=logging.INFO)

    @wraps(ori_func)
    def wrapper(*args, **kwargs):
        logging.info('ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return ori_func(*args, **kwargs)
    return wrapper


def my_timer(ori_func):
    import time
    import logging

    @wraps(ori_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = ori_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(ori_func.__name__, t2))
        logging.info('ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return result

    return wrapper


@my_logger
@my_timer
def display_multi_args(name, gender, age):
    time.sleep(1)
    print('display_multi_args function executed with multiple args ({}, {}, {})'.format(
        name, gender, age))


display_multi_args('Jean', 'F', 54)
