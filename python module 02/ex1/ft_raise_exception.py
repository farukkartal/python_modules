#!/usr/bin/env python

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp > 40):
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif (temp < 0):
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    try:
        value_1 = "25"
        print(f"Input data is '{value_1}'")
        temp_1 = input_temperature(value_1)
        print(f"Temperature is now {temp_1}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    try:
        value_2 = "abc"
        print(f"Input data is '{value_2}'")
        temp_2 = input_temperature(value_2)
        print(f"Temperature is now {temp_2}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        value_3 = "100"
        print(f"Input data is '{value_3}'")
        temp_3 = input_temperature(value_3)
        print(f"Temperature is now {temp_3}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        value_4 = "-50"
        print(f"Input data is '{value_4}'")
        temp_4 = input_temperature(value_4)
        print(f"Temperature is now {temp_4}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
