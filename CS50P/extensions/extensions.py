def get_media_type(file_name):
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Extract the file extension
    suffix = file_name.lower().replace(' ', '').rsplit('.', 1)[-1]
    full_suffix = '.' + suffix if '.' not in suffix else suffix

    # Return the corresponding media type or default if not found
    return media_types.get(full_suffix, 'application/octet-stream')

def main():
    file_name = input("Enter the name of the file: ")
    media_type = get_media_type(file_name)
    print(f"{media_type}")

if __name__ == "__main__":
    main()
