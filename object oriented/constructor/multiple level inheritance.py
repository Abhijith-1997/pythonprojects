#Multiple inheritane/hierarchial inheritance
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Employee(Person):
    def det(self,company,place):
        self.company=company
        self.place=place
        print(self.company)
        print(self.place)
class Vehicle(Employee):
    def car(self,brand,colour):
        self.brand=brand
        self.colour=colour
        print(self.brand)
        print(self.colour)
per=Person()
per.details("abhi",23)
emp=Employee()
emp.det("luminar","kakkanad")
emp.details("arun",23)
veh=Vehicle()
veh.details("bijoy",23)
veh.det("luminartech","kochi")
veh.car("tata","blue")
