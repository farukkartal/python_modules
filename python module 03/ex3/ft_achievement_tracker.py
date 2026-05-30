#!/usr/bin/env python3

import random

ALL_ACH = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind",
    "Hidden Path Finder", "Unstoppable"
]


def gen_player_achievements() -> set:

    x = random.randint(5, 10)
    selected_ach = random.sample(ALL_ACH, x)
    return (set(selected_ach))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice_ach = gen_player_achievements()
    bob_ach = gen_player_achievements()
    charlie_ach = gen_player_achievements()
    dylan_ach = gen_player_achievements()
    print(f"Player Alice: {alice_ach}")
    print(f"Player Bob: {bob_ach}")
    print(f"Player Charlie: {charlie_ach}")
    print(f"Player Dylan: {dylan_ach}\n")
    global_ach = alice_ach.union(bob_ach, charlie_ach, dylan_ach)
    common_ach = alice_ach.intersection(bob_ach, charlie_ach, dylan_ach)
    print(f"All distinct achievements: {global_ach}\n")
    print(f"Common achievements: {common_ach}")
    only_alice = alice_ach.difference(bob_ach, charlie_ach, dylan_ach)
    only_bob = bob_ach.difference(alice_ach, charlie_ach, dylan_ach)
    only_charlie = charlie_ach.difference(alice_ach, bob_ach, dylan_ach)
    only_dylan = dylan_ach.difference(alice_ach, bob_ach, charlie_ach)
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")
    full_ach_set = set(ALL_ACH)
    alice_missing = full_ach_set.difference(alice_ach)
    bob_missing = full_ach_set.difference(bob_ach)
    charlie_missing = full_ach_set.difference(charlie_ach)
    dylan_missing = full_ach_set.difference(dylan_ach)
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")
