#person child parent student
# child parent=person
#student class=child

class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Child(Person):
    def det(self,address,place):
        self.address=address
        self.place=place
        print(self.address)
        print(self.place)
class Parent(Person):
    def view(self,id,district):
        self.id=id
        self.district=district
        print(self.id)
        print(self.district)
class Student(Child):
    def stutdet(self,state):
        self.state=state
        print(self.state)
per=Person()
per.details("abhi",23)
ch=Child()
ch.det("payyanur","kannur")
ch.details("arun",21)
p=Parent()
p.view(1001,"kannur")
stud=Student()
stud.stutdet("Kerala")
stud.det("payyanur","kozhikode")
stud.details("bijoy",20)


