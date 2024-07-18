def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations_dictionary = dict(
    {
        '+' : add
        ,
        '-' : subtract
        ,
        '*' : multiply
        ,
        '/' : divide
    }
)

def calculator():
    num1 = float(input("Enter the first number : "))

    for operators in operations_dictionary:
        print(operators)

    flag = True

    while flag:
        operator = input("Enter the operator : ")

        num2 = float(input("Enter the second number : "))

        calculator_function = operations_dictionary[operator]

        output = calculator_function(num1, num2)

        print(f"{num1} {operator} {num2} = {output}")

        choice = input(f"Enter 'Y' to continue calculation with {output}, 'N' to start a new calculation, 'X' to exit : ").lower()

        if choice == 'y':
            num1 = output
        elif choice == 'n':
            flag = False
            calculator()
        else:
            flag = False

calculator()