from datetime import date, datetime
import sys
import inflect

def get_date_of_birth():
    """Prompts the user for their date of birth and returns it as a date object."""
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        return datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        sys.exit(1)

def calculate_age_in_minutes(dob, current_date):
    """Calculates the age in minutes given the date of birth and the current date."""
    delta = current_date - dob
    age_in_days = delta.days
    age_in_minutes = age_in_days * 24 * 60
    return round(age_in_minutes)

def convert_to_words(number):
    """Converts a number to words using inflect, removing the word 'and'."""
    p = inflect.engine()
    words = p.number_to_words(number)
    return words.replace(" and ", " ").capitalize()

def print_age_in_words(age_in_words):
    """Prints the age in words."""
    print(age_in_words)

def main():
    dob = get_date_of_birth()
    today = date.today()
    age_in_minutes = calculate_age_in_minutes(dob, today)
    age_in_words = convert_to_words(age_in_minutes)
    print_age_in_words(age_in_words +  " minutes")

if __name__ == "__main__":
    main()
