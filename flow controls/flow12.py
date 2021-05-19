num1=int(input("enter the number"))
num2=int(input("enter ur number"))
num3=int(input("enter the number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
     print("largest number",num2)
    else:
        print("largest number",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
     print("largest number",num1)
    else:
        print("largest number",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("largest number",num1)
    else:
        print("largest number",num2)


