# Week 1 Assignment: Basic Calculator Program

# The program will ask the user to input two numbers and a mathematical operation (+, -, *, /).
# It will then perform the operation and display the result.

# Prompt the user to input the first number and store it as a float for decimal compatibility
num1 = float(input("Enter the first number: "))

# Prompt the user to input the second number and store it as a float for decimal compatibility
num2 = float(input("Enter the second number: "))

# Prompt the user to input the mathematical operation (addition, subtraction, multiplication, or division)
operation = input("Enter the operation (+, -, *, /): ")

# Use if-elif statements to check the operation and perform the appropriate arithmetic

if operation == "+":
    # If the operation is addition, add num1 and num2
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")  # Display the result of the addition

elif operation == "-":
    # If the operation is subtraction, subtract num2 from num1
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")  # Display the result of the subtraction

elif operation == "*":
    # If the operation is multiplication, multiply num1 and num2
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")  # Display the result of the multiplication

elif operation == "/":
    # If the operation is division, check if num2 is not zero to avoid division by zero error
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")  # Display the result of the division
    else:
        print("Error: Division by zero is not allowed!")  # Error message for division by zero

else:
    # If the operation is not recognized, display an error message
    print("Error: Invalid operation entered. Please use +, -, *, or /.")
