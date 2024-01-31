import validators

def validate_email():
    email = input("Enter your email address: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

def main ():
    validate_email()
if __name__ == "__main__":
    main()
