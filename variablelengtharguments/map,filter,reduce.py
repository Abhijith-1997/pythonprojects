# map
# arr=[2,3,4,5,6]
# squarelist=list(map(lambda num:num**2,arr))
# print(squarelist)

# lst=["abhi","ranjith","rajila"]
# uppername=list(map(lambda name:name.upper(),lst))
# print(uppername)

# lst=[3,7,9,8,5]
# op=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(op)

#filter

# lst=[3,7,9,8,5]
# even=list(filter(lambda num:num%2==0,lst))
# print(even)
# lst=["abhi","ranjith","rajila"]
# name=list(filter(lambda name:name[0]=="a",lst))
# print(name)
#print employee name
# from functools import reduce
employee=[
     {"eid":1000,"name":"abhi","salary":25000,"desig":"developer"},
     {"eid": 1001, "name": "arun", "salary": 26000, "desig": "qa"},
     {"eid": 1002, "name": "varun", "salary": 27000, "desig": "ba"}]
# highsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
#           list(map(lambda emp:emp["salary"],employee)))
# print(highsal)

ename=[emp["name"]for emp in employee]
print(ename)



# name=list(map(lambda  emp:emp["name"],employee))
# print(name)
# # upp=list(map(lambda name:name.upper[0],name))
# # print(upp)
# developer=list(filter(lambda emp:emp["salary"]>23000,employee))
# print(developer)
# developer=list (filter(lambda emp:emp["desig"]=="developer" and emp["salary"]>24000,employee))
# print(developer


      #functools
# arr=[1,2,3,4,5,6,7]
# from functools import*
# highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
# print(highest)
# total=reduce(lambda  num1,num2:num1+num2,arr)
# print(total)


fruits=["mango","orange","apple"]
f=[(fruit,fruit,fruit)for fruit in fruits]
print(f)
ar=[1,2,3,14,17,18]
sqr=[num**2 for num in ar]
print(sqr)
lst1=[1,2]
lst2=[10,20]
list=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(list)

even=[num for num in ar if num%2==0]
print(even)
lst=[7,8,9,4,3,1]
lst1=[num+1 if num>5 else num-1 for num in lst]
print(lst1)