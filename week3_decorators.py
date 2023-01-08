# def square(a):
#     return a**2

# print(square(7))
# l=[1,2,3,4]
# print(list(map(square,l)))

# def my_map(func,l):
#     new_l=[]
#     for item in l:
#         new_l.append(func(item))
#     return new_l

# print(my_map(square,l))

# def outer_func():
#     def inner_func():
#         print('inside inner func ')
#     return inner_func

# var=outer_func()
# var()

# def outer_func2(msg):
#     def inner_func2():
#         print(f"message is {msg}")
#     return inner_func2

# var1=outer_func2('Hi there')
# var1()

# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# power=to_power(3)
# print(power(2))

# # decorators intro
# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome function')
#         any_function ()
#     return wrapper_function
# @decorator_function
# def func1():
#     print('this is func1')
# func1()
# var=decorator_function(func1)
# var()

# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         """this is awesome functio"""
#         print('this is awesome function')
#         # any_function (*args,**kwargs)
#         return any_function (*args,**kwargs)
#     return wrapper_function
# @decorator_function
# def func(a):
#     print(f'this is function with agument {a}')
# func(7)

# @decorator_function
# def add(a,b):
#     ''''this is add function'''
#     return a+b
# # print(add(4,5))
# print(add.__doc__)
# print(add.__name__)

# from functools import wraps
# def print_function_data(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f"You are calling {function.__name__}")
#         print(f"{function.__doc__}")
#         return function(*args,**kwargs)
#     return wrapper

# @print_function_data
# def add(a,b):
#     '''This function takes two numbers as arguments and return their sum'''
#     return a+b
# print(add(4,5))

# Excercise1
from functools import wraps
import time 
def calculate_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"Executing {function.__name__}")
        t1=time.time()
        returned_value=function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"This function took {total_time} seconds ")
        return returned_value
    return wrapper
@calculate_time
def square(n):
    return [i**10 for i in range(1,n+1)]

print(square(100))
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args,**kwargs)
        print("Invalid argument")

        data_types=[]
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print("Invalid argument")
    return wrapper

@only_int_allow
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add_all(1,2,3,4,5,[1,2,3]))
print(add_all(1,2,3,4,5))

# Decorators with arguments in Python
from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print("Invalid argument")
        return wrapper
    return decorator
@only_data_type_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string+=i
    return string
print(string_join('rahul','gupta'))




























