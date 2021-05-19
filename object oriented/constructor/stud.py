class Student:
    collegename="sdit"
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def printval(self):
        print(self.rollno)
        print(self.name)
        print(self.course)
        print("college",Student.collegename)
stud=Student(1001,"abhi","mca")
stud.printval()