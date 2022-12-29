s={1,2,3,2}
print(s)
print(s[1]) # we can't use index in sets
l=[1,2,3,4,5,5,5,5,6,7,7,8]
#remove duplicate
s2=set(l)
s2=list(set(l))
print(s2)

s={1,2,3}
s.add(4)
print(s)
s.add(5)
print(s)


s.remove(3) # here if i put a non element than error 
s.discard(4)  # here if i put non elemnt then it will not give any error
print(s)

s.clear()
print(s)

s1=s.copy()
print(s1)

s={'a','b','c'}
if 'a' in s:
    print("present")
else:
    print("not present")

for item in s:
    print(item)

s1={1,2,3,4}
s2={3,4,5,6}
# union
union_set=s1|s2
print(union_set)

#intersection
print(s1&s2)

# list comprehensions
squares=[]
for i in range(1,11):
    squares.append(i**2)

print(squares)

squares2=[i**2 for i in range(1,11)]
print(squares2)

negative=[]
for i in range(1,11):
    negative.append(-i)

print(negative)

negative1=[-i for i in range(1,11)]
print(negative1)

names=['Rahul','Mohit','Rohan']
new_list=[]
for name in names:
    new_list.append(name[0])

print(new_list)

new_list2=[name[0] for name in names]
print(new_list2)

# Excercise 1
def reverse_str(l):
    return [name[::-1] for name in l]

print(reverse_str(['abc','tuv','xyx']))

# List Comprehension with if statement in Python
numbers=list(range(1,11))
num=[i for i in numbers if i%2==0]

even_num=[i for i in range(1,11) if i%2==0]
print(even_num)
print(num)

odd_num=[i for i in range(1,11) if i%2!=0]
print(odd_num)

# excercise 2 
def num_to_string(l):
    return [str(i) for i in l if (type(i)==int or type(i)== float) ]
l=[True,False,[1,2,3],1,1.0,3]
print(num_to_string(l))

#  List comprehension with if else in Python
nums=list(range(1,11))

new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

new_list2=[i*2 if(i%2==0) else -i for i in nums]
print(new_list2)

# Nested list comprehension in Python
example=[[1,2,3],[1,2,3],[1,2,3]]

nested_comp=[[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

nested2=[[i for i in range(1,4)], [j for j in range(11,14)]]
print(nested2)

#  Dictionary Comprehension in Python
square={num:num**2 for num in range(1,11)}
print(square)
square={f"square of {num} is":num**2 for num in range(1,11)}
print(square)

string="Rahul Gupta"
word_count={char:string.count(char) for char in string}
print(word_count)

odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

# Sets comprehension in Python
s={k**2 for k in range(1,12)}
print(s)
names1=['Rahul','Vijay']
frst={name1[0] for name1 in names1}
print(frst)



