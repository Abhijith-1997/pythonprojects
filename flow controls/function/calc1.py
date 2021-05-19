def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("select operator")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
while True:
    choice=input("enter the choice")
    if choice in("1","2","3","4"):
        num1=float(input("enter the number"))
        num2=float(input("eneter the number"))
        if choice=="1":
            print(add(num1,num2))
        elif choice=="2":
            print(sub(num1,num2))
        elif choice=="3":
            print(mul(num1,num2))
        elif choice=="4":
            print(div(num1,num2))
        break
else:
    print("invalid")