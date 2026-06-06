#!/usr/bin/env python3

def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                data = file.read()
                return (True, data)
        elif action == "write":
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Error: Unsupported action")
    except PermissionError:
        return (False, f"[Errno 13] Permission denied: '{file_name}'")
    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory: '{file_name}'")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0] is True:
        print(secure_archive("new_archive.txt", "write", result[1]))
