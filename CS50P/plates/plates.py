def is_valid(vanity_plate):
    """
    Function to validate if a vanity plate is valid based on the given conditions.
    """
    # Check if the length of the plate is between 2 and 6 characters
    if not (2 <= len(vanity_plate) <= 6):
        return False

    # Check if the plate starts with at least two letters
    if not (vanity_plate[0].isalpha() and vanity_plate[1].isalpha()):
        return False

    # Check for no periods, spaces, or punctuation marks
    if not vanity_plate.isalnum():
        return False

    # Check that numbers, if present, are at the end and do not start with '0'
    number_started = False
    for char in vanity_plate:
        if char.isdigit():
            if char == '0' and not number_started:
                # First number cannot be '0'
                return False
            number_started = True
        elif number_started:
            # Numbers cannot be in the middle of a plate
            return False

    return True
def main():
    plate = input("Plate: ")
    if is_valid(plate.upper()):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
