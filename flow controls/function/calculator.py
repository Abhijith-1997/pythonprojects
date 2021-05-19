def add():
    a=int(input("enter the number"))
    b=int(input("enterthe number"))
    print(a+b)
def sub():
    a = int(input("enter the number"))
    b = int(input("enterthe number"))
    print(a - b)
def mul():
    a = int(input("enter the number"))
    b = int(input("enterthe number"))
    print(a*b)
def div():
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a/b)
operator=input("enter th operator")
if(operator=="+"):
    add()
elif(operator=="-"):
    sub()
elif(operator=="*"):
    mul()
elif(operator=="/"):
    div()
else:
    print("invalid")




