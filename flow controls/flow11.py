sex=input("enter ur sex")
mstatus=input("married or not")
if(sex=='m'):
    age=int(input("enter ur age"))
    if(20<=age<=40):
        print("work in any where")
    elif(40<=age<=60):
         print("work in urban area")
    else:
        print("error")
elif(sex=='f'):
    print("urban area")
else:
    print("error")

