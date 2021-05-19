# import re
# n=input("enter the string")
# x="(^a[a-zA-z0-9\w]*b$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter")
# x="^[A-Z][a-z]*"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("vaild")
# else:
#     print("invalid")

#
import re
r=open("ph","r")
f=open("number", "w")
x="([+][9][1]\d{10})"
for num1 in r:
     number=num1.rstrip("\n")
     n=re.finditer(x,num1)
     if n!=None:
         f.write(number)
         f.write("/")
# class Book:
#     def bookdetails(self,libraryname,bookname,author):
#         self.libraryname=libraryname
#         self.bookname=bookname
#         self.author=author
#     def printval(self):
#         print(self.libraryname)
#         print(self.bookname)
#         print(self.author)
# b=Book()
# b.bookdetails("pppp","the jungle","james")
# b.printval()

# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def printval(self):
#         print(self.name)
#         print(self.type)
# class Dog(Animal):
#     def __init__(self,color,age,name,type):
#         super().__init__(name,type)
#         self.color=color
#         self.age=age
#     def print(self):
#         print(self.color)
#         print(self.age)
# a=Dog("jack","jerman","golden",1)
# a.print()
# a.printval()
#
# class Book:
#     def details(self,bname,author):
#         self.bname=bname
#         self.author=author
#         print("bname",self.bname)
#         print("author",self.author)
#         print("bad")
# class Type(Book):
#     def details(self,bname,author):
#         self.bname=bname
#         self.author=author
#         print("bname",self.bname)
#         print("author",self.author)
#         print("good")
# book=Type()
# book.details("fghj","ghjk")

# class Person:
#     def det(self,name):
#         self.name=name
#         print(self.name)
# class Print(Person):
#     def m(self,age):
#         self.age=age
#         print(self.age)
# class Student:
#     def details(self,course):
#         self.course=course
#         print(self.course)
# class Employee(Person,Student):
#     def print(self,salary):
#         self.salary=salary
#         print(self.salary)
# class Manager(Employee):
#     def printval(self,place):
#         self.place=place
#         print(self.place)
# p=Person()
# p.det("abhi")
# d=Print()
# d.m(23)
# s=Student()
# s.details("mca")
# e=Employee()
# e.det("arun")
# e.details("bca")
# e.print(10000)
# m=Manager()
# m.det("bijoy")
# m.details("Mca")
# m.print(12000)
# m.print("payyanur")
#


# class Student:
#     def __init__(self,name,rollno,course,mark):
#         self.name=name
#         self.rollno=rollno
#         self.course=course
#         self.mark=mark
#         print(self.name)
#         print(self.rollno)
#         print(self.course)
#         print(self.mark)
# lst=[]
# f=open("phone","r")
# for i in f:
#     d=i.rstrip("\n").split(",")
#     name=d[0]
#     rollno=d[1]
#     course=d[2]
#     mark=d[3]
#     s1=Student(name,rollno,course,mark)
#     lst.append(s1)
# mark=[]
# for st in lst:
#     mark.append(st.mark)
# print(mark)
# for st in lst:
#     if(st.mark==max(mark)):
#         print(st.name,st.rollno,st.course,st.mark)

# import re
# f2=open("result","w")
# rule="([l][u][m]\d{2}[p][y]\d{3}$)"
# f=open("sub","r")
# for num in f:
#     number=num.rstrip("\n")
#     matcher=re.fullmatch(rule,number)
#     if matcher!=None:
#         f2.write(number)
#         # f2.write("\n")