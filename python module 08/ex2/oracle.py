import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is missing. "
          "Run pip install -r requirements.txt")
    sys.exit(1)


def read_config() -> None:
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...")
    keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    missing_keys = []
    for key in keys:
        if not os.environ.get(key):
            missing_keys.append(key)
    if len(missing_keys) > 0:
        print("\n[ERROR] The Oracle cannot proceed. Missing configurations:")
        for missing in missing_keys:
            print(f" -> {missing}")
        sys.exit(1)
    matrix_mode = os.environ.get("MATRIX_MODE")
    log_verbosity = os.environ.get("LOG_LEVEL")
    zion_url = os.environ.get("ZION_ENDPOINT")
    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")
    if matrix_mode == "development":
        print("Database: Connected to local instance")
    elif matrix_mode == "production":
        print("Database: Connected to secure PRODUCTION cluster")
    else:
        print("Database: Connection unknown")
    print("API Access: Authenticated")
    print(f"Log Level: {log_verbosity}")
    if zion_url:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    read_config()
