import sys
import random
from pyfiglet import Figlet

def bad_exit():
    print("Invalid usage")
    sys.exit(1)

figlet = Figlet()
argc = len(sys.argv)

if argc != 3 and argc != 1:
    bad_exit()
elif argc==3:
    output = sys.argv[1]
    font = sys.argv[2]
    # Check the option argument
    if output not in ["-f", "--font"]:
        bad_exit()
    # Set the font
    if str(font) in figlet.getFonts():
        figlet.setFont(font=font)
        str = input("Input: ")
        print("Output:\n", figlet.renderText(str))
    else:
        bad_exit()
elif argc==1:
    str = input("Input: ")
    available_fonts = list(Figlet().getFonts())
    random_font = random.choice(available_fonts)
    figlet.setFont(font=random_font)
    print("Output:\n", figlet.renderText(str))
