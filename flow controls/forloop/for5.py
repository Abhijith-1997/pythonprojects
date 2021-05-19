low=int(input("enter low"))
up=int(input("enter up"))
sumeven=0
sumodd=0
for i in range(low,up+1):
    if(i%2==0):
        sumeven=sumeven+i
    else:
         sumodd=sumodd+i
print(sumeven)
print(sumodd)

