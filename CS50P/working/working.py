import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression for matching and parsing the input string
    pattern = r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)'
    match = re.fullmatch(pattern, s)

    # Raise ValueError if the input format is incorrect
    if not match:
        raise ValueError("Invalid format")

    # Extract hours, minutes, and meridiem indicators
    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()

    # Convert hours and minutes to integers, setting minutes to 0 if not provided
    start_hour, end_hour = int(start_hour), int(end_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    # Validate time values
    if not (0 <= start_hour <= 12 and 0 <= start_minute < 60 and 0 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError("Invalid time")

    # Convert 12-hour format to 24-hour format
    start_hour = (start_hour % 12) + (12 if start_meridiem == 'PM' else 0)
    end_hour = (end_hour % 12) + (12 if end_meridiem == 'PM' else 0)

    # Construct the converted time string
    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"

if __name__ == "__main__":
    main()
