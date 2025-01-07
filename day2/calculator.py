print("Select operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Input")
