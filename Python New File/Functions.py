# #print 1 to 10 numbers in functions
# def num1(start, end):
#     for i in range(start, end+1):
#         print(i)
# print(num1(1,10))

# #print 10 to 1 by using Functions
# def sam(start, end):
#     for i in range(start, end, -1):
#         print(i)
# print(sam(10,1))
#
# #print even length inside a list:
# l = ["python","java", "selenium", "c++"]
# #l1 = []
# def func(l):
#     l1 = []
#     for i in l:
#         if len(i)%2==0:
#             l1.append(i)
#     return l1
# print(func(l))
#

# #print Charecter and its index by using functions
# def func(args):
#     for i, j in enumerate(args):
#         print (i, j)
#
# func('hello world')



# #take a string and reverse that string inside function
#
# def func(string):
#     res = ""
#     for item in string:
#         res = item+res
#     return res
# print(func("hai"))

# # Check a  number is prime or not
# def prime_(num):
#     for i in range(2,num):
#         if num%i==0:
#             return ("not a prime")
#         return (f"num is prime {num}")
# print(prime_(3))


# waf to print sum of n numbers

# def sum_(num):
#     sum = 0
#     for item in range(num):
#         last_ = (num) % 10
#         sum += last_
#         num = num//10
#     return sum
# print(sum_(456))

#
# #To print digits in a string in a function
# def string_(args):
#     # st = "Hello 123 program 345"
#     for item in args:
#         if item.isdigit():
#             print(item)
# string_("Hello 123 program 345")
#
#
# # count special char in the string
# def special_(args):
#     c = 0
#     for item in args:
#         if not ("0"<=item<="9" or  "a"<=item<="z" or "A"<=item<="Z"):
#             print(item)
#             c+=1
#             print(c)
# special_("Hello$#%^&* 123 program 345")
#
#

# #wap program to count capitals and loewrcase
# def func(args):
#     lc= 0
#     ac= 0
#     for i in args:
#         if "a"<=i<="z":
#             lc+=1
#
#         elif "A"<=i<="Z":
#             ac+=1
#     print(ac)
#     print(lc)
# print(func("HAi HAello"))

# #by using inbuilt method
# def func(args):
#     upper_=0
#     lower_=0
#     for i in args:
#         if i.islower():
#             lower_+=1
#         elif i.isupper():
#             upper_+=1
#     print(upper_)
#     print(lower_)
# func("HAi HAello")

#
# def pali_(args):
#     if args == args[::-1]:
#         print("poli")
#     else:
#         print("not a poli")
# pali_("mom")

# def poli_(args):
#     res = ""
#     for i in args:
#         res = i+res
#     if res == args:
#         print("poli")
#     else:
#         print("not a poli")
# poli_("dad")

#
#
# #waf which returns even numbers from 1 to 50:
# l = []
# def evens(start = 1,end = 51):
# #     for
#
#
#
# def prime_(start, end):
#     l = []
#     for num in range(start, end+1):
#         for item in range(2, num):
#             if num%item==0:
#                 print(f"{num}not a prime")
#                 break
#             else:
#                 # print(f"{num}prime")
#                 print(l.append(num))
#
#
#
# # prime_(2,10)
# # print(l)
#
#
# def prime(start, end ):
#     list_=[]
#     for num in range(start, end+1):
#         for i in range(2, num):
#             if num%i==0:
#                 # print("not a prime")
#                 break
#         else:
#             list_.append(num)
#     print(list_)
#
#
# prime(2, 10)
#
# list_ = []
# for num in range(2, 10):
#     for i in range(2, num):
#         if num % i == 0:
#             # print("not a prime")
#             break
#     else:
#         list_.append(num)
# print(list_)



def spam(func):
    def wrapper(*args,**kwargs):
        print("hai Hello")
        return func(*args, **kwargs)
    return wrapper
@spam
def loans(balance):
    return balance
print(loans("10000"))

















