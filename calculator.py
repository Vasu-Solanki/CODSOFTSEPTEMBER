def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"
    return x / y

def remainder(x, y):
    if y == 0:
        return "Error!"
    return x % y


def calculator():
    print('''Select operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Remainder''')

    choice = int(input("Enter choice (1/2/3/4): "))
    
    if choice > 4:
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
        operator = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operator = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operator = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operator = "/"
    elif choice == 5:
        result = remainder(num1, num2)
        operator = "%"

    print(f"{num1} {operator} {num2} = {result}")

for_repeating = True

while for_repeating:
    
    calculator()
    repeat = str(input("Would you like to do more calculations. type 'Yes' or 'No'. ")).lower()
    if repeat == "yes":
        pass
    
    elif repeat == "no":
        for_repeating = False
    
    else:
        print("Please! Enter a valid input.")    
    
    