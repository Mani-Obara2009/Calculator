"""A simple and bite-sized calculator for the command line."""

def calculator(number1, number2, operation):
    """Calculate the result of an operation between two numbers."""
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
    elif operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "**":
        return number1 ** number2
    elif operation == "ROOT":
        return number1 ** (1 / number2)
    elif operation == "/":
        return number1 / number2
    else:
        return "Unknown operator. Type 'HELP' for options."


# Interactive loop
while True:
    try:
        n1 = float(input("Enter your first number: "))
        n2 = float(input("Enter your second number: "))
        operator = input("Enter your operator (type HELP for options): ").upper().strip()

        result = calculator(n1, n2, operator)
        print(f"Result: {result}")

    except ValueError as e:
        print(f"❌ Invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"🚫 Division by zero: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
