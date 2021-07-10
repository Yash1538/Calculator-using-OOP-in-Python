# simple calculator using OOP in python
class calculator:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def add(self):
        addition = self.var1 + self.var2
        print("addition: ", addition)

    def sub(self):
        subtraction = self.var1 - self.var2
        print("subtraction: ", subtraction)

    def multiply(self):
        multiplication = self.var1 * self.var2
        print("multiplication: ", multiplication)

    def div(self):
        division = self.var1 / self.var2
        print("division: ", division)


a = int(input("Enter 1st Variable: "))
b = int(input("Enter 2nd Variable: "))

cal = calculator(a, b)  # created object "cal" of class "calculator"

while True:
    n = int(input("1.ADD 2. SUB 3.MUl 4. DIV 5.Exit\n"))
    if n == 1:
        cal.add()
    elif n == 2:
        cal.sub()
    elif n == 3:
        cal.multiply()
    elif n == 4:
        cal.div()
    elif n == 5:
        exit()
    else:
        print("Please Enter valid Argument")
