# 42. Menu-driven program: Calculator (+, -, *, /).
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")

ch = input("Enter yor choice :")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

if ch == '+':
    print(f"{num1} + {num2} = {num1 + num2}")

elif ch == '-':
    print(f"{num1} - {num2} = {num1 - num2}")

elif ch == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif ch == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("invelid choice")