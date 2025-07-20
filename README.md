```markdown
# Python Command-Line Calculator

A simple yet powerful command-line calculator implemented in Python that supports basic arithmetic operations, exponents, and roots.

## Features

- Basic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Advanced operations:
  - Exponentiation (**)
  - Nth root (ROOT)
- Interactive help system (type HELP)
- Error handling for invalid inputs and division by zero

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mani-Obara2009/Calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Calculator
   ```

## Usage

Run the calculator:
```bash
python calculator.py
```

Follow the prompts:
1. Enter your first number
2. Enter your second number
3. Enter an operator (type HELP for supported operators)

### Supported Operators

| Operator | Description               | Example Input |
|----------|---------------------------|---------------|
| +        | Addition                  | 5 + 3 → 8     |
| -        | Subtraction               | 5 - 3 → 2     |
| *        | Multiplication            | 5 * 3 → 15    |
| /        | Division                  | 6 / 3 → 2     |
| **       | Exponentiation            | 2 ** 3 → 8    |
| ROOT     | Nth root (1st num √ 2nd)  | 8 ROOT 3 → 2  |
| HELP     | Show help message         | HELP          |

## Error Handling

The calculator handles:
- Division by zero attempts
- Invalid numeric inputs
- Unknown operators
- Other unexpected errors

## Example Session

```
Enter your first number: 8
Enter your second number: 3
Enter your operator: ROOT
2.0

Enter your first number: 10
Enter your second number: 0
Enter your operator: /
You can't divide by zero!
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License

Completely open source ❤️ 
In the mission of spreading kindness and open software culture.
