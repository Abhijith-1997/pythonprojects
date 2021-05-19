#single inheritance
class Person:                          #super class/base class/ payment class
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):                     # derived class/sub class/child class
    def print(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)
per=Person()
per.setval("abhi",23,"male")
st=Student()
st.print("mca","sdit")
st.setval("arun",23,"male")


