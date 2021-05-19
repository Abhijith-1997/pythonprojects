# num1=int(input("enter the range"))
# num2=int(input("enter the range"))
# for i in range(num1,num2+1):
#     if(i%2==0):
#         for j in range(num1,num2+1):
#             print()
#             for k in range(0,j):
#                 print(i,end="")
#     else:
#         for j in range(num1,num2+1):
#             print()
#             for k in range(num2+1,j,-1):
#                 print(i,end="")

a=int(input("enter the range"))
b=int(input("enter the range"))
for i in range(a,b+1):
    if(i%2==0):
        for j in range(a,b+1):
            print()
            for k in range(0,j):
                print(i,end="")
    else:
        for j in range(a,b+1):
            print()
            for k in range(b+1,j,-1):
                print(i,end="")