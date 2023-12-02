import numpy as np
import multiprocessing
from typing import Dict, List
from dataclasses import dataclass

CPU_COUNT = multiprocessing.cpu_count()

target: Dict[str, int] = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Game:
    red: int = 0
    green: int = 0
    blue: int = 0


def task_p1(data: str) -> int:
    id: int = int(data.split(":")[0].split(" ")[1])

    games: List[Game] = [
        Game(**{color: int(num) for num, color in pairs})
        for pairs in (
            [j.strip().split(" ") for j in i.split(", ")]
            for i in data.split(":")[1].split(";")
        )
    ]

    def is_valid(game: Game) -> bool:
        return all(getattr(game, color) <= target[color] for color in target.keys())

    if all(map(is_valid, games)):
        return id

    return 0


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p1, data)

    with open("data/data_output_1.txt", "w") as f:
        for i in range(len(results)):
            f.write(f"{data[i]} = {results[i]}\n")

    print(f"Part 1 Solution: {sum(results)}")


def task_p2(data: str) -> int:
    games: List[Game] = [
        Game(**{color: int(num) for num, color in pairs})
        for pairs in (
            [j.strip().split(" ") for j in i.split(", ")]
            for i in data.split(":")[1].split(";")
        )
    ]

    def min_set(games: List[Game]) -> int:
        return np.prod(
            [max(getattr(game, color) for game in games) for color in target.keys()]
        )

    return min_set(games)


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p2, data)

    with open("data/data_output_2.txt", "w") as f:
        for i in range(len(results)):
            f.write(f"{data[i]} = {results[i]}\n")

    print(f"Part 1 Solution: {sum(results)}")


if __name__ == "__main__":
    part_1()
    part_2()
