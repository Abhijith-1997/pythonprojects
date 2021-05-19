# class Parent:
#     def properties(self):
#         print("10 lackd rs,2 car")
#     def marry(self):
#         print("with abhi")
# class Child(Parent):
#     def marry(self):
#         print("with arun")
# c=Child()
# c.marry()

class Vehicle:
    def car(self):
        print("my car is BMW")
    def bike(self):
        print("bike is 350")
class Person(Vehicle):
    def bike(self):
        print("bike is R15")
v=Person()
v.bike()