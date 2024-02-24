import sys
import csv
from tabulate import tabulate

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist.")

def format_csv_table(file_path):
    data = read_csv_file(file_path)
    if not data:
        sys.exit("Error: The CSV file is empty.")

    headers = data[0].keys()
    table = [list(row.values()) for row in data]
    return tabulate(table, headers, tablefmt="grid")

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <file.csv>")

    file_path = sys.argv[1]
    table_str = format_csv_table(file_path)
    print(table_str)

if __name__ == "__main__":
    main()
