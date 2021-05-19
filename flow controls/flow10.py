salary=int(input("enter ur salary"))
year=int(input("enter your service"))
if(year>5):
    salary+=(5/100)*salary
    print("salary is",salary)
else:
    print("salary is",salary)