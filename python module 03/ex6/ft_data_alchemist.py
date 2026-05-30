#!/usr/bin/env python3

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    capitalized_names = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_names}")
    only_capitalized = [name for name in players if name.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}")
    scores = {name: random.randint(1, 1000) for name in capitalized_names}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    rounded_avg = round(average, 2)
    print(f"Score average is {rounded_avg}")
    high_scores = {name: score for name,
                   score in scores.items() if score > average}
    print(f"High scores: {high_scores}")
