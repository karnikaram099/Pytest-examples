# from collections import deque
# from itertools import islice
#
# path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#     n = 4
#     n1 = 3
#     res = islice(file, n)
#     # res1 = deque (file ,n1)
#     print(list(res))
#     # print(list(res1))
#
#
# n =8
# for _ in range(4):
#     print("*"*n)


#
# string = "hellom"
# res = ""
# for i in range(len(string)):
#     res = string[i]+res
# print(res)
#

# st = "hello python"
# res = ""
# for item in range(len(st)):
#     if (item)%2==0:
#         # print (st[item])
#
#
#
# #wad to give input of some delay before of excicuting any function"
# import time
# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)

#         return wrapper
#
#     return (delay)
#
#
# @outer(5)
# def add(a, b):
#     print(a + b)
# def mul(x, y):
#     print(x*y)
#
#
# print(add(3, 5))
# print(mul(4,5))
#


# #wad which takes a string and reverse it
#
# def tax(n):
#     def reve(func):
#         def wrapper(*args, **kwargs):
#             res=func(*args, *kwargs)
#             r = res + ((n/100) * res)
#             return r
#         return wrapper
#     return reve
#
# # @tax(5)
# def sam(amt):
#     return amt
# # def deco(string):
# #     print("srav")
#
#
# print(sam(520))
# # print(deco(f"dear :srav"))
#

#
#
# #if product is more them 1000 discount will be 20%
# #if product is more then 500 discount will be 10%
# def disc(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if res >= 1000:
#             print(res - res*0.20)
#         elif res >= 500:
#             print(res - res*0.10)
#         else:
#             print(res)
#     return wrapper
#
# @disc
# def prod_(price):
#     return price


# print(prod_(550))



# #wAD that caluculates times of excicution of a function.
# import time
# def time_(n):
#     def disc(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             time.sleep(n)
#             reselse:
# #                 print(res)
#             end = time.time()
#             return (f"the total time excicution is:{end-start}")
#         return wrapper
#     return disc
#
# @time_(2)
# def prod_(price):
#     return price
#
#
# print(prod_(1000))
# #
#  = func(*args, **kwargs)
#             if res >= 1000:
#                 print(res - res*0.20)
#             elif res >= 500:
#                 print(res - res*0.10)
# #

# import time
# def disc(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         # time.sleep(n)
#         res = func(*args, **kwargs)
#         if res >= 1000:
#             print(res - res * 0.20)
#         elif res >= 500:
#             print(res - res * 0.10)
#         else:
#             print(res)
#         end = time.time()
#         return (f"the total time excicution is:{end - start}")

#     return wrapper
#
# @disc
# def prod(cost):
#     return cost
#
# def add(a, b):
#     return a+b
#
# def sub(c, f):
#     return(c-f)
#
#
#
# print(prod(1000))
# print(add(7,5))
# # print(sub(5 ,4))
# #
#
# def arg(func):
#     def wrapper(*args, **kwargs):
#         # res = func(*args , **kwargs)
#         func(*args, **kwargs)
#         res = (len(args)+len(kwargs))
#         return((res))
#     return wrapper
# @arg
# def sam(name, surname):
#
#     return name
#
# @arg
# def demo(a = "10", b = "20"):
#     return demo



# def add(a, b, c, d):
#    return a+b+c+d
#
# print(demo)
#
#
# print(sam("Ram", "karnika"))
# print(add(10, 2, 45, 3))


# def prime(n):
#     def sam(func):
#         def wrapper(*args, **kwargs):
#             for i in range(2,n):
#                 if n%i==0:
#                     return False
#             return True
#         return wrapper
#     return sam
# @prime(17)
# def fam():
#     return
#
# print(fam())


#
# def sam(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return len(res)
#     return wrapper
#
# @sam
# def demo(name):
#     return name
#
# print(demo("ram"))
#



# def sam(msg = "hello world"):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             print(msg)
#             return func(*args, **kwargs)
#         return wrapper
#     return log
#
# @sam()
# def add():
#     return
#
# print(add())



