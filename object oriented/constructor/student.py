class Student:
    def __init__(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def printval(self):
        print("name of student",self.name)
        print("rollno",self.rollno)
        print("course",self.course)
    def __str__(self):
        return self.name+str(self.rollno)
stud=Student("abhi",1001,"python")
stud.printval()
print(stud)