# # # # import os
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# # # # with open(path) as file:
# # # #     count = 0
# # # #     for line in file:
# # # #         a = line.split()
# # # #         for word in a:
# # # #             if word[0].lower() in "aeiou":
# # # #                 count+=1
# # # #     print(count)
# # # # #
# # # # #
# # # #
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"
# # # # with open(path) as file:
# # # #     d = {}
# # # #     count = 0
# # # #     for item in file:
# # # #         list_=item.split()
# # # #         for word in set(list_):
# # # #             count+=1
# # # #             d[word]=count
# # # #     print(d)
# # # #
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"
# # # # with open(path) as file:
# # # #     for word in file:
# # # # #         data = word.split("- -")
# # # # #         # print(data)
# # # # #         print(data[0])
# # # #
# # # #
# # # #
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# # # # with open(path) as file:
# # # #     for line in file:
# # # #         print(line)
# # #
# # #
# # #
# # #
# # #
# # #
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# # # # with open(path)as file:
# # # #     count=1
# # # # #     for item in file:
# # # # #         count+=1
# # # # #         print(count)
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# # # # from collections import deque
# # # # with open(path)as file:
# # # #     lines = deque(file,4)
# # # #     print(list(lines))
# # #
# # # #
# # # # def fact(n):
# # # #     if n==0 or n==1:
# # # #         return 1
# # # #     return n*fact(n-1)
# # # # print(fact(5))
# # #
# # # #
# # # # def sum(n):
# # # #     if n==1:
# # # #         return 1
# # # #     return n+sum(n-1)
# # # # print(print(sum(5))
# # # #
# # # #
# # # # def sum(n):
# # # #     if n==1:
# # # # #         return 1
# # # # #     return n+sum(n-1)
# # # # # print(sum(25))
# # # # def rev_st (st, i=0, res=" "):
# # # #      if i>=len(st):
# # # #          return(res)
# # # #      res = st[i]+res
# # # #      return rev_st(st, res, i+1)
# # # # print(rev_st("hai hello how are you"))
# # #
# # # #
# # # # path_f = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\football.txt"
# # # # with open(path_f ,encoding = "UTF-8") as file:
# # # #     for line in file:
# # # #         if line.strip():
# # # #             country = line.split("\t")
# # # #             print(country[1], end=" ")
# # # #
# # #
# # #
# # # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# # # # from collections import defaultdict,Counter
# # # # d = defaultdict(int)
# # # #
# # # # with open(path) as file:
# # # #     for line in file:
# # # #         if line.strip():
# # # #             words = line.split()
# # # #             for word in words:
# # # #                 d[word] += 1
# # # # print(d)
# # # # c = Counter(d)
# # # # most, *rest, least = c.most_common()
# # # # print(most, least)
# # #
# # #
# # # """ 1st"""
# # # # import csv
# # # # e_path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# # # # with open(e_path)as file:
# # # #     r_obj = csv.reader(file)
# # # #     header = next(r_obj)
# # # #     print(header)
# # # #     for row in r_obj:
# # # #         if int(row[3])>70000:
# # # #             print(row[0])
# # #
# # # """2nd"""
# # # """wap to group male and female empoloyes"""
# # import csv
# # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# # # with open(path) as file:
# # #     r_obj = csv.reader(file)
# # #     header = next(r_obj)
# # #     d = {"male":[], "female":[]}
# # #     for row in r_obj:
# # #         if row[1]=="male":
# # #             d["male"] += [row[0]]
# # #         else:
# # #             d["female"] += [row[0]]
# # #     print(d)
# #
# #
# # # """by using defaultdict"""
# # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# # # from collections import defaultdict
# # # with open(path) as file:
# # #     r_obj = csv.reader(file)
# # #     header = next(r_obj)
# # #     dd = defaultdict(list)
# # #     for row in r_obj:
# # #         dd[row[1]] += [row[0]]
# # # print(dd)
# #
# # # """wap group the employess based on their teams"""
# # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# # # from collections import defaultdict
# # # with open(path) as file:
# # #     r_obj = csv.reader(file)
# # #     header = next(r_obj)
# # #     dd = defaultdict(list)
# # #     for row in r_obj:
# # #         dd[row[2]] += [row[0]]
# # # print(dd)
# #
# #
# # # """normal method"""
# # # path = r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# # # d = {}
# # # with open(path) as file:
# # #     r_obj = csv.reader(file)
# # #     for row in r_obj:
# # #         if row[2] not in d:
# # #             d[row[2]]=[row[0]]
# # #         else:
# # #             d[row[2]] += [row[0]]
# # # # print(d)
# # # """based on price"""
# # # import csv
# # # path = r"C:\Users\karni\PycharmProjects\Python New File\File Handliing\.csv"
# # # with open(path) as file:
# # #     read_obj = csv.DictReader(file)
# # #     # print(list(read_obj))
# # #     l = list(read_obj)
# # #     res = sorted(l, key=lambda d: float(d["price"]))
# # #     print(list(res))
# #
# #
# # #
# # # def test(i, j):
# # #     if i == 0:
# # #         return j
# # #     else:
# # #         return test(i-1, i+j)
# # # print(test(4, 7))
# # #
# # #
# # #
# # # path =r"C:\Users\karni\PycharmProjects\Alpha_3\dictionariess.py"
# # # print(path)
# # #
# # #
# # # #
# # # def num(n):
# # #     a = 0
# # #     b = 1
# # #     # i = 0
# # #     while a <= n:
# # #         print(a)
# # #         c = a+b
# # #         a = b
# # #         b = c
# # #         # i+=1
# # # print(num(10))
# # #
# # #
# # #
# # #
# # # def prime(num):
# # #     # if i > 1:
# # #         for i in range(2, num):
# # #             if i > 1:
# # #                 if num%i==0:
# # #                     return "not a prime"
# # #         return "prime"
# # #
# # # print(prime(58))
# #
# # #
# # # # def prime_(num):
# # # for num in range(10):
# # #     if num >1:
# # #         for i in range(2, num):
# # #             if num % i == 0:
# # #                 break
# # #         else:
# # #             print(num)
# # #
# # # # print(prime_(10))
# #
# # #print("abcdef".center(10))
# #
# #
# # # def prime(end, start=2):
# # #     res = for n in range(start, end+1):
# # #         if n>1:
# # #             for i in range(2, n):
# # #                 if n % i== 0:
# # #                     break
# # #             else:
# # #                 res.append(n)
# # #     return res
# # # print(prime(start = 1, end = 50))
# #
# #
# # #
# # # from turtle import*
# # # color("red")
# # # begin_fill()
# # # pensize(3)
# # # left(50)
# # # forward(133)
# # # circle(50,200)
# # # right(140)
# # # circle(50, 200)
# # # forward(133)
# # # # end_fill()
# # #
# # #
# # # dict_ = {"a":1, "b":2}
# # # # for i in dict_:
# # # #     print(dict_.keys())
# # #
# # #
# # #
# # # d ={dict_.values() for i in dict_}
# # # print(d)
# #
# #
# # # names = {"apple", "google", "apple", "yahoo", "gmail", "gmail", "gmail"}
# # # d = {}
# # # for index, item in enumerate(names):
# # #     d[item] = [index]
# # # print(d)
# #
# #
# # #
# # # s = [(4, 56, 78 ), ("one", "two", "three")]
# # # l1, l2 = s
# # # print(l1)
# # # print(l2)
# # # d = {l2[index] : l1[index] for index in range(len(l2))}
# # # print(d)
# # import math
# #
# # #print(round(51.49))
# # #print(math.(52.99))
# #
# #
# # #
# # # st = "hello evrone how are you"
# # # #print(len(st))
# # # # print(st[::-1])
# # #
# # #
# # #
# # # b = "hai"
# # # b = "hai"
# # # # print(b)
# # # # print(id(b))
# # # # a=b
# # # # print(id(a.split()))
# #
# #
# #
# # # # b = " "
# # # # print(b.isspace())
# # #
# # # # a = ["hai"]
# # # # a.join(["hello", "hai"])
# # # a = "hai"
# # # b = "hello"
# # # c = [a,b]
# # # #print((c))
# # # print("".join(c))
# # #
# # #
# # # l = ["hai", "hello", 1, 2, 3]
# # # l1 = []
# # # for index, item in enumerate(l):
# # #     l1.append((index,item))
# # # print(l1)
# # #
# # # l = ["hai", "hello", 1, 2, 3]
# # # lc = [(index, item) for index, item in enumerate(l)]
# # # print(lc)
# #
# #
# #
# # l = ["hai", "hello", "happyy"]
# # l1 = []
# # for item in l:
# #     if len(item) % 2 == 0:
# #         l1.append(item)
# #     else:
# #         l1.append((item[::-1]))
# # print(l1)
# # #
# # l = ["hai", "hello", "happyy"]
# # lc = [item if len(item)%2==0 else(item[::-1]) for item in l]
# # print(lc)
# #
# #
# #
# #
# #
# #
# #
# # def rev_string(st, res=" ", i = 0):
# #     if i>len(st):
# #         return res
# #     res = st[i]+res
# #     return ((rev_string(st, res, i+1))
# #
# # print(rev_string("hello hai"))
#
#
# # def sum_(num, sum=0):
# #     if num > 0:
# #         last = num % 10
# #         sum += last
# #         num = num // 10
# #         return sum_(num, sum)
# #     else:
# #         return sum
#
# # print(sum_(456))
#
# # def count_(start, end):
# #     if start > end:
# #         return
# #     print(start)
# #     count_(start+1, end)
# #
# # count_(1, 10)
# #
#
#
#
# # def sum(n):
# #     if n == 1:
# #         return 1
# #     return n+sum(n-1)
# # print(sum(5))
#
# #
# # def sum_n(n, sum=0):   # 4
# #     if n > 0:
# #         sum += n
# #         return sum_n(n-1, sum)
# #     return sum
# #
# # print(sum_n(5))
#
#
# #
# # def count_digits(num, count=0):
# #     if num > 0:
# #         count += 1
# #         return count_digits(num//10, count)
# #     return count
# #
# # print(count_digits(123))
#
#
#
#
#
#
#
# #
# #
# # l = ["hai", "hello", "happyy"]
# # for i in l:
# #     if len(i) % 2 == 0:
# #         print
#
#
# #
# # def count_(start, end):
# #     if start < end:
# #         return
# #     print(start)
# #     count_(start-1, end)
# #
# # count_(-1, -10)
#
# #
# # def count_(start, end):
# #     if start>end:
# #         return
# #     print(start)
# #     count_(start+1, end)
# # print(count_(1, 10))
# # #
# #
# #
# # def fact(n):
# #    if n==0 or n==1:
# #        return 1
# #    return n*fact(n-1)
# # print(fact(5))
# #
# #
#
#
# #
# # multi = lambda num1, num2 :num1*num2
# # print(multi(4, 5)
# #
# #
# # element = lambda charecter:charecter[-1]
# # print(element("helloooi"))
# #
# #
# # palindrome = lambda i: i==i[::-1]
# # print(palindrome("mok"))
#
#
#
#
# string = "hai im {} and im from {}".format("ram",   "Kurnool")
# print(string)
#
#
#
# data = "hello {} you are selected for {} and u r package is {}".format("Madhuri", "Sony", "6lpa")
# print(data)
# #
#
# a = "hai"
# print(a.join("hello world"))
# path = r"C:\Users\karni\PycharmProjects\Python New File\venv\pyvenv.cfg"
import time


def sample(func):
    def wrapper(*args, **kwargs):
        print("hey hai")
        func(*args, **kwargs)
    return wrapper
@sample
def demo(a, b):
    print(a*b)

print(demo(2, 5))


#wad to give input of some delay before of excicuting any function"
def outer(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            func(*args, **kwargs)
#         return wrapper
#     return(delay)
#
# @outer(5)
# def add(a, b):
#     print(a+b)
#
#
# def mul(x, y):
#     print(x*y)
#
#
# print(add(3, 5))
# print(mul(4,5)














import re
a = re.findall(r"a+b", "abababababab       aaaaaaabbbbbbb")
print(a)











