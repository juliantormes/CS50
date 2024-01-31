def main():
    while True:
        try:
            n = int(input("Size: "))
            if 0 < n < 9:  # Adjusted to accept n greater than 0 and less than 9
                break
            elif n >= 9:
                print("Enter a value lower than 9")
            else:
                print("Enter a value greater than 0")
        except ValueError:
            print(
                "Invalid input. Please enter a valid integer."
            )  # Inform the user of the error.

    for i in range(n):
        print(" " * (n - 1 - i) + "#" * (i + 1) + "  " + "#" * (i + 1))


if __name__ == "__main__":
    main()
