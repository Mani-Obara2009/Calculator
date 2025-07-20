import math
while True:
    # Taking some inputs
    n1 = int(input("Enter your first number : "))
    n2 = int(input("Enter your second number : "))
    operator = input("Enter your operator (To see the supported ones, type help) : ").upper().strip()

    def calculator(n1, n2, operator):
        n3 = 1 / n2
        if operator == "HELP":
            return "You can type '+' and '-' and '*' for multipeling\n and '**' for powering the first number to the second number\n and 'root' for getting the root of first number with the index of the second number\n and for deviding simply use the symbol '/'"
        elif operator == "+" :
            return n1 + n2
        elif operator == "-":
            return n1 - n2
        elif operator == "*" :
            return n1 * n2
        elif operator == "**":
            return n1 ** n2
        elif operator == "ROOT":
            return n1 ** n3
        elif operator == "/":
            return n1 / n2
        else :
            return "There was an error with your inputs, If you think this is an error, contact me on mani.obara.work@gmail.com"

    print(calculator(n1 , n2 , operator))