#constructor :to initialise instance variable
#constructor automaticallly invoke when creating object
class Person:
     def __init__(self,name,age,gender):
         self.name=name
         self.age=age
         self.gender=gender
     def printval(self):
         print(self.name)
         print(self.age)
         print(self.gender)
per=Person("abhi",24,"male")
per.printval()

