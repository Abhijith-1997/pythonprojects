class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Vehicle:
    def car(self,brand,colour):
        self.brand=brand
        self.colour=colour
        print(self.brand)
        print(self.colour)
class Child(Person,Vehicle):
    def info(self,place,district):
        self.place=place
        self.district=district
        print(self.place)
        print(self.district)
per=Person()
per.details("abhi",23)
veh=Vehicle()
veh.car("tata","white")
ch=Child()
ch.details("bijoy",23)
ch.car("bmw","black")
ch.info("payyanur","kannur")