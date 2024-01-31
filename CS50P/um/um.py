import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Using regular expression to find all standalone occurrences of 'um' (case-insensitive)
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
