class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Mobile:
    def print(self):
        print("i have note4")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
per=Person()
per.details("abhi",23)
mob=Mobile()
mob.print()
ch=Child()
ch.details("arun",23)
ch.print()
ch.info("sdit","mangalore")