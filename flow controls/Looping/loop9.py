num=int(input("enter the number"))
print(num)
sum=0
while(num!=0):#154
    rem=num%10
    sum=(sum*10)+rem
    num=num//10
print(sum)
