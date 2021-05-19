# class Student:
#     def stud(self,id,name,college):
#         self.id=id
#         self.name=name
#         self.college=college
#     def printval(self):
#         print("id=",self.id)
#         print("name=",self.name)
#         print("college=",self.college)
# obj=Student()
# obj.stud(1001,"abhi","sridevi")
# obj.printval()
#
# obj1=Student()
# obj1.stud(1002,"arun","sridevi")
# obj1.printval()

#yype of variables

#instance variable related to methods
#class variable related to class
class Student:
    college="sridevi"
    def stud(self,id,name):
        self.id=id
        self.name=name

    def printval(self):
        print("id=",self.id)
        print("name=",self.name)
        print("college=",Student.college)
obj=Student()
obj.stud(1001,"abhi")
obj.printval()

obj1=Student()
obj1.stud(1002,"arun" )
obj1.printval()

