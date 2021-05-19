num=int(input("enter the num"))
fact=1
if(num<0):
     print("not factorial")
elif(num==0):
        print("factorial 0 is 1")
else:
      for i in range(1,num+1):
        fact=fact*i
      print("factorial of",num,"is",fact)


