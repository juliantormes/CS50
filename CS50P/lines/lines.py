import sys

def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit(f"Error: The specified file '{filename}' does not exist.")

    lines_of_code = 0

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        lines_of_code += 1

    return lines_of_code

def main ():
    if len(sys.argv) != 2:
        sys.exit("Usage: python count_lines.py <filename.py>")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Error: The specified file does not have a .py extension.")

    try:
        line_count = count_lines_of_code(filename)
        print(f"{line_count}")
    except FileNotFoundError:
        sys.exit(f"Error: The specified file '{filename}' does not exist.")

if __name__ == "__main__":
    main()
