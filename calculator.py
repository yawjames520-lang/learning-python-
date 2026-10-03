# learning-python-
My Beginner Python Practice projects:  calculator, quiz game,  and more..
# A simple calculator: the user picks two numbers and an operation,
# and the program calculates the answer.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: you can't divide by zero"
    return a / b


num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
op = input("Choose +, -, *, / : ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(subtract(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))
else:
    print("Invalid operation")
