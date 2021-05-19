a=[1,2,3,4,5,6,7]
b=[7,8,3,5]
c=[]
for i in b:
    if i in a:
        c.append(i)
print(c)