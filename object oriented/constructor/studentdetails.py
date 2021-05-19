class Student:
    def details(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return self.name
f=open("student", "r")
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    stud=Student()
    stud.details(name,age)
    print(stud)
    stud.printval()

