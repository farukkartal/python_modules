import sys
import os
import site


def test() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows")
            print("Then run this program again.")
        else:
            venv_name = os.path.basename(sys.prefix)
            print("\nMATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}\n")
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")
            print("Package installation path:")
            paths = site.getsitepackages()
            if len(paths) > 0:
                print(paths[0])
            else:
                print("Unknown path")
    except Exception as e:
        print(f"A matrix glitch occurred: {e}")


if __name__ == "__main__":
    test()
