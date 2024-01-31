import sys
from PIL import Image, ImageOps

def valid_extension (input_file, output_file):
    # Check if input and output file extensions are valid
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    if not input_file.lower().endswith(tuple(valid_extensions)) or not output_file.lower().endswith(tuple(valid_extensions)):
        sys.exit("Input and output files must have valid extensions (.jpg, .jpeg, .png).")
    if input_file.lower().split('.')[-1] != output_file.lower().split('.')[-1]:
        sys.exit("Input and output have different extensions")
    else:
        return True
def overlay_shirt(input_file, output_file):
    # Check if input file exists
    try:
        with Image.open(input_file) as img_input:

            shirt = Image.open("shirt.png")

            # Resize and crop input image to match shirt size
            img_input = ImageOps.fit(img_input, shirt.size)

            # Overlay the shirt image on the input image
            img_input.paste(shirt, shirt)

            # Save the result
            img_input.save(output_file)
            print("Image overlay successful.")
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        sys.exit(1)
def main():
    # Check if there are exactly two command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python overlay_shirt.py <input_image> <output_image>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if  valid_extension (input_file, output_file) :
        overlay_shirt(input_file, output_file)

if __name__ == "__main__":
    main()

