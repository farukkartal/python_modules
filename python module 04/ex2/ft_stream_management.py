#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 ft_stream_management.py <file>")
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file'{file_name}'")

        try:
            file = open(file_name)
            content = file.read()
            print("---")
            print(content, end="")
            if len(content) > 0 and not content.endswith('\n'):
                print()
            print("---")
            file.close()
            print(f"File '{file_name}' closed.")
            new_content = content.replace('\n', '#\n')
            if len(content) > 0 and not content.endswith('\n'):
                new_content += '#'
            print("Transform data:")
            print("---")
            print(new_content, end="")
            if len(new_content) > 0 and not new_content.endswith('\n'):
                print()
            print("---")
            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()
            new_file_name = sys.stdin.readline()
            new_file_name = new_file_name.replace('\n', '')
            if new_file_name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to'{new_file_name}'")
                try:
                    new_file = open(new_file_name, "w")
                    new_file.write(new_content)
                    new_file.close()
                    print(f"Data saved in file '{new_file_name}'.")
                except PermissionError:
                    print(f"[STDERR] Error opening file'{new_file_name}': "
                          f"[Errno 13] Permission denied:'{new_file_name}'",
                          file=sys.stderr)
                    print("Data not saved")

        except FileNotFoundError:
            print(f"[STDERR] Error opening file'{file_name}': "
                  f"[Errno 2] No such file or directory:'{file_name}'",
                  file=sys.stderr)

        except PermissionError:
            print(f"[STDERR] Error opening file'{file_name}': "
                  f"[Errno 13] Permission denied:'{file_name}'",
                  file=sys.stderr)
