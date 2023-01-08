# def nums(n):
#     for i in range(1,n+1):
#         # print(i)
#         yield(i)
# nums(10)
# print(nums(10))
# for number in nums(10):
#     print(number)
# numbers=nums(10)
# for num in numbers:
#     print(num)

# excercise 1
# def even_generator(n):
#     for num in range(2,n+1,2):
#         yield(num)
#     # for num in range(1,n+1):
#     #     if num%2==0:
#     #         yield(num**2)

# for num in even_generator(20):
#     print(num)

# Generator Comprehension in Python
# square=(i**2 for i in range(1,11))
# # print(square)
# for num in square:
#     print(num)
# for num in square:
#     print(num)

# List vs Generators in Python
import time
# t1=time.time()
# l=[i**2 for i in range(10000000)]
# t2=time.time()
# print(t2-t1)

t1=time.time()
g=(i**2 for i in range(10000000))
t2=time.time()
print(t2-t1)


