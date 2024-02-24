import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression for validating an IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Check if the IP address matches the pattern
    if re.match(pattern, ip):
        # Split the IP address into octets
        octets = ip.split('.')

        # Check each octet to be in the range 0 to 255
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()
