import multiprocessing
from functools import partial
from typing import Dict, Tuple, List

CPU_COUNT = multiprocessing.cpu_count() // 2

stages = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def task_p1(data: Dict, seed: int) -> int:
    stage_input: int = seed

    for stage in stages:
        for destination_range, source_range, range_length in data[stage]:
            if source_range <= stage_input < source_range + range_length:
                stage_input = destination_range + (stage_input - source_range)
                break

    return stage_input


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        seeds = list(
            map(int, f.readline().split(":")[1].strip(" ").strip("\n").split(" "))
        )
        data = f.read().strip("\n")

    data_dict = {
        k.split(" ")[0]: [
            [int(num) for num in group.split()] for group in v.strip().split("\n")
        ]
        for k, v in (d.split(":") for d in data.split("\n\n"))
    }

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(partial(task_p1, data_dict), seeds)

    print(f"Part 1 Solution: {min(results)}")


def task_p2(data: Dict, seed: List[Tuple[int, int]]) -> int:
    i = 0
    while True:
        stage_input: int = i
        for stage in reversed(stages):
            for destination_range, source_range, range_length in data[stage]:
                if destination_range <= stage_input < destination_range + range_length:
                    stage_input = source_range + (stage_input - destination_range)
                    break

        for ranges in range(len(seed)):
            if seed[ranges][0] <= stage_input <= seed[ranges][1]:
                return task_p1(data, stage_input)

        i += 1


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        seeds = list(
            map(int, f.readline().split(":")[1].strip(" ").strip("\n").split(" "))
        )
        data = f.read().strip("\n")

    data_dict = {
        k.split(" ")[0]: [
            [int(num) for num in group.split()] for group in v.strip().split("\n")
        ]
        for k, v in (d.split(":") for d in data.split("\n\n"))
    }

    seed_ranges: List[Tuple[int, int]] = [
        (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
    ]

    results = task_p2(data_dict, seed_ranges)

    print(f"Part 2 Solution: {results}")


if __name__ == "__main__":
    part_1()
    part_2()
