dict={'name':'abhi','age':23,'class':'first'}
key=input("nter the key")
flag=0
for i in dict:
    if i==key:
        flag=1
        break
if flag==1:
    print("key found")
else:
    print("keyis not found")



