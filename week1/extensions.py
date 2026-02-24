def main() -> None:
    """Main part of the program"""

    file_name = input("File name: ").lower().strip()
    print_media_type(file_name)


def print_media_type(file_name: str) -> None:
    """Print the media type of file"""
    extension = file_name.split(".")[-1]

    if extension == "gif" or extension == "png":
        print(f"image/{extension}")
    elif extension == "jpg" or extension == "jpeg":
        print("image/jpeg")
    elif extension == "pdf" or extension == "zip":
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
