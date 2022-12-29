def total(a,b):
    return a+b

print(total(5,6)) # this is good as only two requirements
print(total(5,6,7,10)) # this will give error this is where args* come in play

def all_total(*args):
     total=0
     for num in args:
        total+=num
     return total

print(all_total(1,2,3))
print(all_total(1,2,3,4))


def multipl_nums(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(multipl_nums(1,2,3))
print(multipl_nums(1,2,3,4))

def multipl_nums(num,*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(multipl_nums(2,2,4))
print(multipl_nums(2,2,4,4)) # here when we put a new parameter with args it wiil not be counted in args and will be treated separately

def multiply_nums(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply

nums=[2,3,4]
print(multiply_nums(nums)) # on doing like this we will not get desired result
print(multiply_nums(*nums)) # we van use * for unpacking the list 

# excercise 1 
def cube_num(num,*args):
    print(type(args))
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass args"
nums=[2,3,4]
print(cube_num(2,*nums))

#  ** Kwargs in Python
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")

d={'name':'Rahl','age':20}

func(first_name="Rahul",last_name="Gupta")
func(**d)

# correct order of Function with all type of parameters in Python

def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Rahul',1,2,3,a=1,b=2)

# excercise 2
def func(string):
    return [i.capitalize() for i in string]

names=['rahul','gupta']
# print(func(names))

def func(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


print(func(names,reverse_str=True))

