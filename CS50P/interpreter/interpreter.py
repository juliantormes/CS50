def calculate_expression(x, operator, z):
    """
    This function takes two integers (x, z) and an arithmetic operator (+, -, *, /),
    and returns the result of the arithmetic operation.
    """
    try:
        # Converting x and z to integers
        x = int(x)
        z = int(z)
    except ValueError:
        return "x and z must be integers."

    # Performing the arithmetic operation
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z == 0:
            return "Division by zero is not allowed."
        result = x / z
    else:
        return "Invalid operator. Use +, -, *, or /."

    # Returning the result formatted to one decimal place
    return f"{result:.1f}"

def main():
    # Asking the user for an expression
    expression = input("Enter an arithmetic expression (x y z): ")

    # Splitting the input into parts
    parts = expression.split()
    if len(parts) != 3:
        print("Invalid input format. Please enter in 'x y z' format.")
        return

    x, operator, z = parts

    # Calculating and displaying the result
    result = calculate_expression(x, operator, z)
    print(result)
    
if __name__ == "__main__":
    main()
