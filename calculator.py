"""A clean and extensible command-line calculator."""

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y
def power(x, y): return x ** y
def root(x, y): return x ** (1 / y)

# Operator mapping dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "ROOT": root
}

# Help message
HELP_MESSAGE = """
🧮 Supported operations:
+       : Addition
-       : Subtraction
*       : Multiplication
/       : Division
**      : Power (x ** y)
ROOT    : y-th root of x (same as x ** (1/y))
HELP    : Show this message
QUIT    : Exit the calculator
"""

def calculator(x, y, operator):
    """Perform calculation based on the operator."""
    if operator == "HELP":
        return HELP_MESSAGE
    if operator in operations:
        return operations[operator](x, y)
    return "❓ Unknown operator. Type HELP to see options."


# ---- Main Loop ----
print("🔢 Welcome to the Command-Line Calculator!")
while True:
    try:
        # First number input
        n1_input = input("Enter the first number (or 'quit'): ").strip().lower()
        if n1_input in ('quit', 'exit'):
            print("👋 Exiting calculator. Goodbye!")
            break

        # Second number input
        n2_input = input("Enter the second number (or 'quit'): ").strip().lower()
        if n2_input in ('quit', 'exit'):
            print("👋 Exiting calculator. Goodbye!")
            break

        # Operator input
        operator = input("Enter operator (+, -, *, /, **, ROOT) or HELP/QUIT: ").strip().upper()
        if operator in ('QUIT', 'EXIT'):
            print("👋 Exiting calculator. Goodbye!")
            break

        # Convert inputs to floats
        number1 = float(n1_input)
        number2 = float(n2_input)

        # Perform the operation
        result = calculator(number1, number2, operator)
        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Invalid number. Please enter a valid numeric value.")
    except ZeroDivisionError:
        print("🚫 Division by zero is not allowed.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
