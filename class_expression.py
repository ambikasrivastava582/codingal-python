class Expression:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def calculate(self):
        if self.op == "+":
            return self.a + self.b
        elif self.op == "-":
            return self.a - self.b
        elif self.op == "*":
            return self.a * self.b
        elif self.op == "/":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid Operator"


# Example
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

exp = Expression(x, y, op)
print("Result =", exp.calculate())
