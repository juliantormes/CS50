import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Adjusted regular expression pattern to match YouTube URLs specifically within iframe src attributes
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    # If a match is found, return the shorter youtu.be URL
    if match:
        video_id = match.group(1)
        return f'https://youtu.be/{video_id}'

    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()
