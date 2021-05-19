class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Company(Employee):
    def __init__(self,companyname,place,name,age):
        super().__init__(name,age)
        self.companyname=companyname
        self.place=place
    def print(self):
        print("companyname",self.companyname)
        print("place",self.place)
emp=Company("luminar","kakkanad","bijoy",23)
emp.printval()
emp.print()
