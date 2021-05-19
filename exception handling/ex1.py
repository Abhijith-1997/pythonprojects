# num1=int(input("enter"))
# num2=int(input("enter"))
# try:
#     print(num1/num2)
# except:
#     print("exception occured")

# a=[1,2,3]
# n=int(input("enter the index"))
# try:
#     print(a[n])
# except:
#     print("exception occured")
# finally:
#     print("inside finally")

# try ,exception and finally working same time
try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a+b)
except:
    print("print int values")
finally:
    print("finally")