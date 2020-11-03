import sys
import numbers

class Calculator:
    """ a calc """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

if __name__ == "__main__":
    print("we shall calculate")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.divide,
    ]
    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Pick an operation: ")
        if operation == "q":
            sys.exit()
        op = int(operation)
        a = float(input("pick a number: "))
        b = float(input("pick another number: "))
        print(operations[op - 1](a, b))