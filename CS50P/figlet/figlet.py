import sys
import random
from pyfiglet import Figlet

def bad_exit():
    # Print an error message and exit the program
    print("Invalid usage")
    sys.exit(1)

def process_text_with_figlet(argv):
    # Create a new Figlet object
    figlet = Figlet()
    # Count the number of command-line arguments
    argc = len(argv)

    # Check for the correct number of arguments
    if argc != 3 and argc != 1:
        bad_exit()
    elif argc == 3:
        # Extract the command-line arguments
        output = argv[1]
        font = argv[2]

        # Check if the first argument is a font flag
        if output not in ["-f", "--font"]:
            bad_exit()

        # Set the font if it's in the list of available fonts
        if font in figlet.getFonts():
            figlet.setFont(font=font)
            user_input = input("Input: ")
            print("Output:\n", figlet.renderText(user_input))
        else:
            bad_exit()
    elif argc == 1:
        # If no font specified, choose a random one
        user_input = input("Input: ")
        available_fonts = list(Figlet().getFonts())
        random_font = random.choice(available_fonts)
        figlet.setFont(font=random_font)
        print("Output:\n", figlet.renderText(user_input))

def main():
    # Main function to process the text with Figlet
    process_text_with_figlet(sys.argv)

if __name__ == "__main__":
    # Entry point of the script
    main()
