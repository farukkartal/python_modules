#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        print("---\n")
        try:
            file = open(file_name)
            content = file.read()
            print(content, end="")
            file.close()
            print("\n")
            print("---")
            print(f"File '{file_name}' closed.")

        except FileNotFoundError:
            print(f"Error opening file '{file_name}': "
                  f"[Errno 2] No such file or directory: '{file_name}'")

        except PermissionError:
            print(f"Error opening file '{file_name}': "
                  f"[Errno 13] Permission denied: '{file_name}'")
