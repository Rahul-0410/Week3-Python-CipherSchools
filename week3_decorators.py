def square(a):
    return a**2

print(square(7))
l=[1,2,3,4]
print(list(map(square,l)))

def my_map(func,l):
    new_l=[]
    for item in l:
        new_l.append(func(item))
    return new_l

print(my_map(square,l))

def outer_func():
    def inner_func():
        print('inside inner func ')
    return inner_func

var=outer_func()
var()

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var1=outer_func2('Hi there')
var1()

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

power=to_power(3)
print(power(2))