#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")
        pieces = data.split(",")

        if len(pieces) != 3:
            print("Invalid syntax")
        else:
            has_error = False

            for piece in pieces:
                try:
                    float(piece)
                except ValueError as e:
                    print(f"Error on parameter '{piece}': {e}")
                    has_error = True
                    break

            if has_error is False:
                x = float(pieces[0])
                y = float(pieces[1])
                z = float(pieces[2])
                return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {distance:.4f}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{dist_between:.4f}"
    )
