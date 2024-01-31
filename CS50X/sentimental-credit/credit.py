def main():
    cc = 0
    digit_count = 0
    sum = 0
    FirstDigits = 0

    # Get Credit card number
    while cc <= 0:
        try:
            cc = int(input("Number: "))  # This should only accept positive numbers
            if cc <= 0:
                raise ValueError("The number must be a positive integer.")
        except ValueError as e:
            print(e)
            continue  # This will ask for input again if it's not a positive integer

    # checksum
    tmp = cc  # To avoid modifying cc which will be used later
    while tmp > 0:
        digit = tmp % 10
        tmp //= 10
        digit_count += 1
        if 100 > tmp > 10:
            FirstDigits = tmp

        if digit_count % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9

        sum += digit

    # Check length and starting digits
    if sum % 10 == 0:
        if digit_count == 15 and (FirstDigits == 34 or FirstDigits == 37):
            print("AMEX")
        elif digit_count == 16 and 51 <= FirstDigits <= 55:
            print("MASTERCARD")
        elif (FirstDigits // 10) % 10 == 4 and 13 <= digit_count <= 16:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
