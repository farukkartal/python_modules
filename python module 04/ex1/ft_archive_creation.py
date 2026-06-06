#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 ft_archive_creation.py <file>")
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        print("---\n")
        try:
            file = open(file_name)
            content = file.read()
            print(content, end="")
            file.close()
            print("\n\n---")
            print(f"File '{file_name}' closed.")
            new_content = content.replace('\n', '#\n')
            if len(content) > 0 and not content.endswith('\n'):
                new_content += '#'
            print("\nTransform data:")
            print("---\n")
            print(new_content, end="")
            print("\n\n---")
            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")
                try:
                    new_file = open(new_file_name, "w")
                    new_file.write(new_content)
                    new_file.close()
                    print(f"Data saved in file '{new_file_name}'.")
                except PermissionError:
                    print(f"Error opening file '{new_file_name}': "
                          f"[Errno 13] Permission denied: '{new_file_name}'")

        except FileNotFoundError:
            print(f"Error opening file '{file_name}': "
                  f"[Errno 2] No such file or directory: '{file_name}'")

        except PermissionError:
            print(f"Error opening file '{file_name}': "
                  f"[Errno 13] Permission denied: '{file_name}'")
