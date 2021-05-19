class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def printval(self,department,company):
        self.department=department
        self.company=company
        print(self.department)
        print(self.company)
per=Person()
per.setval("abhi",23,"male")
emp=Employee()
emp.printval("ste","luminar")
emp.setval("arun",23,"male")