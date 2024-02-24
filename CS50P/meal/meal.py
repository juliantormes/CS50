def convert(time_str):
    """
    Converts a time string in 24-hour format to the corresponding number of hours as a float.
    For example, "7:30" will be converted to 7.5 hours.
    """
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60.0

def main():
    # Asking the user for a time input
    time_input = input("Enter a time in 24-hour format (#:## or ##:##): ")

    # Converting the time input to hours as a float
    time_in_hours = convert(time_input)

    # Determining and printing the meal time
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")
    # No output if it's not a meal time

if __name__ == "__main__":
    main()
