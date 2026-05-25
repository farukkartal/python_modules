def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    value_1 = "25"
    print(f"Input data is '{value_1}'")
    temp = input_temperature(value_1)
    print(f"Temperature is now {temp}°C")
    print()
    value_2 = "abc"
    print(f"Input data is '{value_2}'")

    try:
        temp2 = input_temperature(value_2)
        print(f"Temperature is now {temp2}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        print()
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
