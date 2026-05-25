#!/usr/bin/env python3
import sys


def process_arguments() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total = len(sys.argv)
    if total == 1:
        print("No arguments provided!")

    else:
        print(f"Arguments received: {total - 1}")
        x = 1
        for arg in sys.argv[1:]:
            print(f"Argument {x}: {arg}")
            x = x + 1
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    process_arguments()
