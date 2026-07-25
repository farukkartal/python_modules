#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[typing.Tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "move", "grab"]
    while True:
        rnd_name = random.choice(names)
        rnd_act = random.choice(actions)
        yield (rnd_name, rnd_act)


def consume_event(
    event_list: typing.List[typing.Tuple[str, str]]
) -> typing.Generator[typing.Tuple[str, str], None, None]:
    while len(event_list) > 0:
        chosen = random.choice(event_list)
        index = 0
        for i in range(len(event_list)):
            if event_list[i] == chosen:
                index = i
                break
        event_list[:] = event_list[:index] + event_list[index+1:]
        yield chosen


def run_events() -> None:
    print("=== Game Data Stream Processor ===")
    event_maker = gen_event()
    for index in range(1000):
        p_name, p_move = next(event_maker)
        print(f"Event {index}: Player {p_name} did action {p_move}")
    batch_of_ten: typing.List[typing.Tuple[str, str]] = []
    for _ in range(10):
        batch_of_ten = batch_of_ten + [next(event_maker)]
    print(f"Built list of 10 events: {batch_of_ten}")
    for current_event in consume_event(batch_of_ten):
        print(f"Got event from list: {current_event}")
        print(f"Remains in list: {batch_of_ten}")


if __name__ == "__main__":
    run_events()
