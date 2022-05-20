# l =[2,3,1]
#
# l1 = [4,5,6]
# # t =(1,2,3)
# res =l+l1
# # print(l+l1)
# print(sorted(res))


# s = "hai"
# res = ''
# for i in s:
#     res = i+res
# print(res)

#
# l =[2,5,7]
# def even(func):
#     def wrapper(*args,**kwargs):
#         def func(*args, **kwargs):
#             res =''
#             for i in l:
#                 if i%2==0:
#                      print("number is even")
#         return func
#     return wrapper
# @even
# def e1(l):
#     print("even numbers")
#
#
# print(e1(2,4))



# class demo:
#     a=10
#     b=20
#     a,b=b,a
#
# print(demo.a)
# # print(demo.b)
#
# import re
# # path= ""
# # with open()
# s = "my emailid is madhuri@gmail.com"
# # res=re.findall('\S+@\S+',s)
#
# # print(res)
#
# # lowercase ,speacial charater,pwd length should be min 8 max 5
# re.findall("[a-z]{8}")



from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("/chromedriver")
driver.get("https://www.google.com/")
