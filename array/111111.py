# lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
# for i in lst:
#     if i[3]>15000:
#         print(i)


# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,6,7,11,34,88]
# for i in a:
#     if i in b:
#         print(i)


# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,7,6,34,289,49,12,63,976]
# lst.sort()
# print(lst)
# print("second largest number is",lst[-2])


# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# lst.sort()
# lst=list(set(lst))
# print(lst)
# eliminate duplicate eliminate
# a=[1,2,3,2,4,5,4,6]
# b=list(set(a))
# print(b)
a={}
f=open("one","r")
for n in f:
    wr=n.split(" ")
    for wor in wr:
        if wor not in a:
            a.update({wor:1})
        else:
            val=int(a[wor])
            val+=1
            a.update({wor:val})
print(a)






