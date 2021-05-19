class Emp:
    company="luminar"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("companyname",Emp.company)
        print(self.salary)
        print(self.name)
        print(self.age)
    def __str__(self):  #two string method
        return self.name+str(self.age)+str(self.salary)
emp=Emp("abhi",23,1000)
emp.printval()
print(emp)