class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1)
        print(self.num2)
    def add(self):
        print(self.num1 + self.num2)
    def sub(self):
        print(self.num1 - self.num2)
    def mul(self):
        print(self.num1 * self.num2)
    def div(self):
        print(self.num1 / self.num2)
calc=Calculator(20,4)
calc.add()
calc.sub()
calc.mul()
calc.div()
