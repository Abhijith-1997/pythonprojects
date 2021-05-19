num=int(input("enter the num"))
sum=0
temp=num
while temp>0:
    digits=temp%10
    sum+=digits**3
    temp//=10
if num==sum:
    print(num,"is amstrong number")
else:
    print(num,"is not amstrong number")