# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print(self.name)
#         print(self.age)
# obj=Person()
# obj.details("anu",23)
# obj.printval()
class Employee:
    company="luminar"
    def details(self,id,name,salary,age,department):
         self.id=id
         self.name=name
         self.salary=salary
         self.age=age
         self.department=department
    def printval(self):
        print(self.id)
        print(self.name)
        print(self.salary)
        print(self.age)
        print(self.department)
        print("company",Employee.company)
obj=Employee()
obj.details(1001,"abhi",10000,23,"stw")
obj.printval()









