def add(a,b):
    return a+b

add2=lambda a,b: a+b
print(add2(5,5))

multiply=lambda a,b: a*b
print(multiply(2,3))

def is_even(a):
    return a%2==0

print(is_even(2))
print(is_even(5))

is_even2=lambda a: a%2==0
print(is_even2(5))

last_char= lambda s: s[-1]
print(last_char("rahul"))

# # lambda with if else 
def func(s):
    if len(s)>5:
        return True
    return False
print(func("ars"))

func1=lambda s: True if len(s)>5 else False
print(func1("abcfeds"))

func2= lambda s: len(s)>5
print(func2("asd"))

#  Enumerate function in Python
names=['abc','abcd','Rahul']
for pos,name in enumerate(names):
    print(f"{pos}-------->{name}")

def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1

names1=['abc','bcd','Rahul']
print(find_pos(names1,'abc'))
print(find_pos(names1,'rahul'))
print(find_pos(names1,'Rahul'))

# Map function in Python
numbers=[1,2,3,4]

def square(a):
    return a**2

squares=list(map(square,numbers))
print(squares)

squares1=list(map(lambda a:a**2,numbers))

print(squares1)

names=['abc','abcd','abcde']
length=map(len,names)
for i in length:
    print(i)

for j in length:
    print(j)

# Filter Function in Python
def is_ven(a):
    return a%2==0

numbers=[3,4,2,1,5,6,9,8,10]
evens=tuple(filter(is_ven,numbers))
evens1=tuple(filter(lambda s:s%2==0,numbers))
print(evens)
print(evens1)

# Zip function in Python
user_id=['user1','user2','user3']
names=['harshit','mohit','rahul']

print(set(list(user_id,names)))

example=[('a',1),('b',2)]
print(dict(example))

l1=[1,3,5,7,]
l2=[2,4,6,8]
new_list=[max(pair) for pair in zip(l1,l2)]
for pair in zip(l1,l2):
   new_list.append(max(pair))

print(new_list)

l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=(list(zip(*l)))
print(list(l1))
print(list(l2))

# Advance Function Practice 1 in Python

# def average_finder(l1,l2):
def average_finder(*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

average_f=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]

print(average_finder([1,2,3],[4,5,6],[7,8,9]))
print(average_f([1,2,3],[4,5,6],[7,8,9]))

# any and all function in Python
number1=[2,4,6,8,10]
number2=[1,2,3,4,5,6]
evens1=[]
for num in number1:
    evens1.append(num%2==0)

print(evens1)

print(all([num%2==0 for num in number1]))

def my_sum(*args):
    if all([(type(arg)== int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "Wrong input"

print(my_sum(1,2,3,4,5,6,7,8,9,['rahul']))
print(my_sum(1,2,3,4,5,6,7,8,9.8))

#  Advance min() and max() in Python
numbers=[1,2,4,5,7]
print(max(numbers))

def func(item):
    return len(item)

name=['Rahulg','Mohit','ab']
print(max(name,key=lambda item:len(item)))
print(min(name,key=lambda item:len(item)))
print(max(name,key=func))

students={
    'rahul':{'score':90,'age':20},
    'mohit':{'score':75,'age':21},
    'rohit':{'score':76,'age':24}
}
print(max(students,key=lambda item: students[item]['score']))

students1=[
    {'name':'rahul','score':90,'age':20},
    {'name':'mohit','score':75,'age':21},
    {'name':'rohit','score':76,'age':24}
]
print(max(students1,key=lambda item:item.get('age'))['name'])

#  Advance sorted function in Python
fruits=['grapes','mango','apple']
fruits.sort()
print(fruits)

fruits2=('grapes','mango','apple')
sorted(fruits2)
print(sorted(fruits2))

fruits3={'grapes','mango','apple'}
print(sorted(fruits3))

guitars=[
    {'model':'yamaha f310','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apollo venis ','price':35000},
    {'model':'taylor 814c ','price':450000}
]
print(sorted(guitars,key=lambda d: d['price'],reverse=True))
print(sorted(guitars,key=lambda d: d['price']))

def add(a,b):
    '''this function takes 2 numbers and return their sum'''
    return a+b

print(add(45,2))

print(add.__doc__)
print(len.__doc__)

help(map)
