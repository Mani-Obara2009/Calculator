"""A simple and bite sized calculator for command line."""
def calculator(number1, number2, operation):
    """This function is used to calculate the result of an operation."""
    if operation == "HELP":
        return (
            "Supported operators:\n"
            "+ : Addition\n"
            "- : Subtraction\n"
            "* : Multiplication\n"
            "/ : Division\n"
            "** : Power (n1 ** n2)\n"
            "ROOT : n2-th root of n1 (same as n1 ** (1/n2))"
        )
    if operation == "+":
        res =  number1 + number2
    if operation == "-":
        res =  number1 - number2
    if operation == "*":
        res =  number1 * number2
    if operation == "**":
        res =  number1 ** number2
    if operation == "ROOT":
        res =  number1 ** (1 / number2)
    if operation == "/":
        res =  number1 / number2
    else:
        res = "Unknown operator. Type 'HELP' for options."
    return res

while True:
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter your second number: "))
    operator = input("Enter your operator (type HELP for options): ").upper().strip()
    try:
        result = calculator(n1, n2, operator)
        print(result)
    except ValueError as e:
        print(f"Invalid input: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ZeroDivisionError as e:
        print(f"Division by zero: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
