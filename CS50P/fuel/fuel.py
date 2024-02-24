def convert(fraction):
    """
    Converts a fraction in the format X/Y to a percentage.
    - X and Y are integers
    - X is not greater than Y
    - Y is not 0
    """
    x, y = map(int, fraction.split('/'))
    # Check if the input meets the conditions
    if x > y:
        raise ValueError("Numerator should not be greater than denominator.")
    elif y == 0:
        raise ZeroDivisionError("Denominator should not be 0.")
    else:
        percentage = (x / y) * 100
        return percentage

def gauge(percentage):
    """
    If 1% or less remains, outputs 'E' (empty).
    If 99% or more remains, outputs 'F' (full).
    """
    # Check for empty or full
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

def main():
        while True:
            fraction = input("Fraction: ")
            try:
                percentage= convert(fraction)
                print(gauge(percentage))
                break
            except ValueError:
                continue
            except ZeroDivisionError:
                continue
if __name__ == "__main__":
    main()
