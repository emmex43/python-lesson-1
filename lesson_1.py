# Basic Calculator Program

# Get user inputs
num1 = float(input("Enter the first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation and display the result
if operator == '+':
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
else:
    print("Invalid operation. Please use one of: +, -, *, /")
