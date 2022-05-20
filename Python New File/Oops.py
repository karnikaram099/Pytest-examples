"""Each substring before excicuting mention with "r" ---> Raw string"""

"""(".")----->it matches with any character except new line"""

"""(sub string$)-----> specify the string is present at the last of the string if its present gives output else it gives empty list"""

"""(^sub string)-----> specify the string is present at the first of the string if its present gives output else it gives empty list)"""

"""(*)---->it specify the prefix character is present at 0 or any number of times"""

"""(+)---->it specify the prefix character is present at 1 or any number of times"""

"""\w or [a-zA-Z0-9_] it specify or it works as a alnum it gives only numbers and alphabets from the string """

"""\W or [^a-zA-Z0-9_] it specify or it gives except alnum """

"""\b it is used for to create a boundary """

"""\w+ it is used for to give the string continuesly seperates at space """

"""("?") will match the occurance of pre character 0 or 1"""

#
#
#
#
#
#
# import re
# #print (dir(re))
# s = re.findall(r".", "hello python")
# #print(s          )#o/p:...............................>['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']
#
#
# s = re.findall(r"^hello", "hello python")
# #print (s)            ..............................>  #o/p:-hello
#
#
#
#
# s = re.findall(r"^python", "hello python")
# #print(s)                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>0/p:-[]
#
#
#
# s = re.findall(r"python$", "hai welcome to python python is very easy and imp is python")
# #print(s)#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>0/p:-['python']
#
#
# s = re.findall(r"\w", "hello python 123234#@&")
# #print(s)           #>>>>>>>>>>>>>>0/p:-['h', 'e', 'l', 'l', 'o', 'p', 'y', 't', 'h', 'o', 'n', '1', '2', '3', '2', '3', '4']
#
#
# s = re.findall(r"\W", "hello python 123234#@&")
# #print(s)            #>>>>>>>>>>>>>>>>>>0/p:-[' ', ' ', '#', '@', '&']
#
#
# s = re.findall(r"\w+", "hello python welcome to python ")
# #print(s)            #>>>>>>>>>>>0/p:-['hello', 'python', 'welcome', 'to', 'python']
#
#
# s = re.findall(r"colou?r","my favorite colour is blue")
# #print(s)            #>>>>>>>>0/p:-['colour']
#
#
# s = re.findall(r"colou?r","my favorite color is blue")
# #print(s)             #>>>>>>>>0/p:-['color']
#
#
# """count the characters in each word ignore the special characters"""
# sentence = "hai welcome & to my world @#$ this is new% python"
# print((re.findall(r"\b[a-z]{3}", sentence)))
# print((re.findall(r"\b[a-z]{3}\b", sentence)))
#
#
# # """find total number of upper case and lowercase alphabets"""
# # sentence= "heLLo woRld welcOMe to pytTHon"
# # upper_count = (len(re.findall(r"[A-Z]", sentence)))
# # lower_count = (len(re.findall(r"[a-z]", sentence)))
# # print(upper_count)
# # print(lower_count)






class one:
    d = 5
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b+self.d
class two(one):
    def __init__(self, a, b, c):
        one.__init__(self,a, b)
        self.c=c
    def add(self):
        return self.c+ self.d+self.b+self.a

class three(two):
    def __init__(self,a,b,c,d,e):
        two.__init__(self, a, b, c)
        self.d = d
        self.e = e
    def add(self):
        return self.c+ self.d+self.b+self.a+self.e+one.d
o = one(4,6)
print(o.add())
t = two(1,2,1)
print(t.add())
tr = three(2,3,4,10,6)
print(tr.add())












