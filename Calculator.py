def calculator(n1, n2, operator):
    if operator == "HELP":
        return (
            "Supported operators:\n"
            "+ : Addition\n"
            "- : Subtraction\n"
            "* : Multiplication\n"
            "/ : Division\n"
            "** : Power (n1 ** n2)\n"
            "ROOT : n2-th root of n1 (same as n1 ** (1/n2))"
        )
    elif operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "**":
        return n1 ** n2
    elif operator == "ROOT":
        return n1 ** (1 / n2)
    elif operator == "/":
        return n1 / n2
    else:
        return "Unknown operator. Type 'HELP' for options."

while True:
    try:
        n1 = float(input("Enter your first number: "))
        n2 = float(input("Enter your second number: "))
        operator = input("Enter your operator (type HELP for options): ").upper().strip()
        result = calculator(n1, n2, operator)
        print("Result:", result)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print("An unexpected error occurred:", e)
        print(f"Unknown error: {e}")