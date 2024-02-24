def get_date():
    while True:
        date_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ").strip()
        if valid_date(date_input):
            return format_date(date_input)
        print("Invalid date, please try again.")

def valid_date(date):
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    try:
        if "/" in date:
            parts = date.split("/")
            if len(parts) != 3:
                return False
            month, day, year = parts
            if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
                return False
        else:
            parts = date.split()
            if len(parts) != 3 or parts[1][-1] != ',':
                return False
            month_name, day, year = parts
            day = day[:-1]  # Remove comma
            if month_name not in months or not day.isdigit() or not (1 <= int(day) <= 31):
                return False
        return len(year) == 4 and year.isdigit()
    except ValueError:
        return False

def format_date(date):
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    if "/" in date:
        month, day, year = date.split("/")
    else:
        month_name, day, year = date.split()
        day = day[:-1]  # Remove comma
        month = months[month_name]

    # Pad single digit day and month with zero
    month = month.zfill(2)
    day = day.zfill(2)

    return f"{year}-{month}-{day}"

def main ():
    formatted_date = get_date()
    print(formatted_date)

if __name__ == "__main__":
    main()
