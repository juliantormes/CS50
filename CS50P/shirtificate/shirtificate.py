from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        # Use Helvetica instead of Arial
        self.set_font('Helvetica', 'B', 12)
        # Updated method call with new_x and new_y
        self.cell(0, 10, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

    def footer(self):
        # This is where you could add a footer if you want
        pass

    def shirtificate(self, name, shirt_image):
        # Add a page
        self.add_page()

        # Assuming the image's size is appropriate and doesn't need resizing
        # You might need to adjust the x, y values to center the image
        img_width = 100
        x_position = (210 - img_width) / 2
        self.image(shirt_image, x_position, 60 , img_width)  # Adjust y to position the image vertically

        # Set the name on top of the shirt, adjusting the positioning as necessary
        self.set_y(80)
        self.set_text_color(255, 255, 255)  # White color
        # Use Helvetica instead of Arial
        self.set_font('Helvetica', 'B', 20)
        # Updated method call with new_x and new_y
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align='C')

if __name__ == "__main__":
    # Ask the user for their name
    name = input("Enter your name: ")
    shirt_image = "shirtificate.png"

    # Create PDF
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.shirtificate(name, shirt_image)

    # Output the PDF
    pdf.output('shirtificate.pdf')
