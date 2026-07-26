#!/usr/bin/env python3
import random


def run_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    capitalized_names = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_names}")
    only_capitalized = [name for name in players if name.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}\n")
    scores = {name: random.randint(1, 1000) for name in capitalized_names}
    print(f"Score dict: {scores}")
    total_score = sum(scores[name] for name in scores)
    average = total_score / len(scores)
    rounded_avg = round(average, 2)
    print(f"Score average is {rounded_avg}")
    high_scores = {name: scores[name] for name in scores if
                   scores[name] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    run_alchemist()
