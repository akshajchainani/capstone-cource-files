
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "cunt"

print("Select operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input("choose (1/2/3/4): ")

num1 = float(input(" first number: "))
num2 = float(input(" second number: "))

if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input")
