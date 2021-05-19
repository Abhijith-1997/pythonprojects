min=int(input("enter the num"))
max=int(input("enter th number"))
sum=0
for a in range(min,max):
    if(a>1):
        for i in range(2,a):
            if(a%i)==0:
                #print("not prime")
                break
        else:
                print(a)
                sum+=a
print("sum of prime number in",min,"to",max,"is",sum)

