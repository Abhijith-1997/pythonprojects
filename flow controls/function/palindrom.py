a=input("enter the string")
temp=a
for i in a:
    rev=a[::-1]
if(temp==rev):
    print("palindrom")
else:
    print("not palindrome")
