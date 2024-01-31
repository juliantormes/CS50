import csv
import sys

STRs = []


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

    # Read database file into a variable
    with open_file(filename1) as db_file:
        reader = csv.DictReader(db_file)

        # Retrieve the DNA sequences (fieldnames) from the CSV, excluding the name field
        STRs = [field for field in reader.fieldnames if field.lower() != "name"]

        # Read the rest of the data from the CSV into a list of dictionaries
        db = list(reader)

    # Read DNA sequence file into a variable
    dna_file = open_file(filename2)
    dna = dna_file.readline().strip()
    dna_file.close()

    # Find longest match of each STR in DNA sequence
    results = {}
    for subseq in STRs:
        results[subseq] = longest_match(dna, subseq)

    # The number of STRs we are checking against
    num_STRs = len(STRs)

    # Check each person in the database for a DNA match
    for person in db:
        if is_dna_match(person, results, STRs, num_STRs):
            print(person["name"])
            return 0

    # If we've gone through all people and found no matches
    print("No match")
    return 0


def is_dna_match(person, results, STRs, num_STRs):
    """
    Check if the DNA sequence matches with the person's STR counts.

    Args:
    person (dict): The person's STR data from the database.
    results (dict): The actual counts of STRs in the DNA sequence.
    STRs (list): The list of STRs.
    num_STRs (int): The number of STRs we are matching against.

    Returns:
    bool: True if there's a match, False otherwise.
    """
    match_count = sum(
        1 for subseq in STRs if int(person.get(subseq, 0)) == results[subseq]
    )

    # If the number of matches is equal to the number of STRs, it's a complete match
    return match_count == num_STRs


def open_file(filename):
    try:
        # Try to open the file
        file = open(filename, "r")
    except OSError:
        # If an error occurs exit with error code 1
        print(f"File {filename} doesn't exist.")
        sys.exit(1)
    else:
        # Return the file pointer
        return file


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
