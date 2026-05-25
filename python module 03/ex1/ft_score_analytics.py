#!/usr/bin/env python3
import sys


def argument_to_int(argument: str) -> int:
    return (int(argument))


def analyze_score() -> None:
    print("=== Player Score Analytics ===")
    total_arg = len(sys.argv)
    if total_arg == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
        return
    approved_scores = []
    for x in sys.argv[1:]:
        try:
            score = argument_to_int(x)
            approved_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{x}'")
    if len(approved_scores) == 0:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {approved_scores}")
    print(f"Total players: {len(approved_scores)}")
    print(f"Total score: {sum(approved_scores)}")
    print(f"Average score: {sum(approved_scores) / len(approved_scores)}")
    print(f"High score: {max(approved_scores)}")
    print(f"Low score: {min(approved_scores)}")
    print(f"Score range: {max(approved_scores) - min(approved_scores)}")


if __name__ == "__main__":
    analyze_score()
