import sys
import csv

def read_csv(input_filename):
    try:
        with open(input_filename, 'r') as input_file:
            reader = csv.reader(input_file)
            next(reader)  # Skip the header row
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        sys.exit(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        sys.exit(f"An error occurred while reading the input CSV: {e}")

def write_csv(output_filename, data):
    try:
        with open(output_filename, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['first', 'last', 'house'])  # Header row for the output CSV
            writer.writerows(data)
        print(f"Data has been converted and saved to {output_filename}")
    except Exception as e:
        sys.exit(f"An error occurred while writing the output CSV: {e}")

def process_data(input_filename, output_filename):
    data = read_csv(input_filename)

    # Process the data to split names
    processed_data = []
    for row in data:
        if len(row) != 2:
            sys.exit("Error: Input CSV should have exactly two columns (name and house).")
        name, house = row
        first_name, last_name = name.split(", ")
        processed_data.append([last_name, first_name, house])

    # Write the processed data to the output CSV
    write_csv(output_filename, processed_data)

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    process_data(input_filename, output_filename)

if __name__ == "__main__":
    main()
