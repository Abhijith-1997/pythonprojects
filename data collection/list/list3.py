list=[1,2,3,4,5,6,7,8,9]
num=int(input("enter the number"))
def linear(x):
    flag=0
    for i in list:
        if i==x:
            flag=1
    if flag==1:
            print("number is found")
    else:
            print("number is not found")
linear(num)


