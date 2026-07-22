#!/usr/bin/env python3

import sys


def parse_inventory() -> dict[str, int]:
    inventory = {}
    for arg in sys.argv[1:]:
        pieces = arg.split(":")
        if len(pieces) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if pieces[0] in inventory:
            print(f"Redundant item '{pieces[0]}' - discarding")
            continue
        try:
            amount = int(pieces[1])
            inventory[pieces[0]] = amount
        except ValueError as e:
            print(f"Quantity error for '{pieces[0]}': {e}")
            continue
    return (inventory)


def display_stats(inv: dict[str, int]) -> None:
    item_list = list(inv.keys())
    print(f"Item list: {item_list}")
    kind = len(inv)
    total = sum(inv.values())
    print(f"Total quantity of the {kind} items: {total}")
    most_item = item_list[0]
    least_item = item_list[0]
    most_quantity = inv[most_item]
    least_quantity = inv[least_item]
    for item in item_list:
        amount = inv[item]
        percentage_rate = (amount / total) * 100
        rounded = round(percentage_rate, 1)
        print(f"Item {item} represents {rounded}%")
        if amount > most_quantity:
            most_quantity = amount
            most_item = item
        if amount < least_quantity:
            least_quantity = amount
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    inv["magic_item"] = 1
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inv = parse_inventory()
    print(f"Got inventory: {inv}")
    display_stats(inv)
