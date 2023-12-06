import numpy as np
import multiprocessing
from typing import Tuple

CPU_COUNT = multiprocessing.cpu_count()


def task(data: Tuple[int, int]) -> int:
    time, distance = data
    result = 0

    for i in range(time + 1):
        if i * (time - i) > distance:
            result += 1

    return result


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        times = list(map(int, f.readline().split(":")[1].strip().split()))
        distances = list(map(int, f.readline().split(":")[1].strip().split()))

    data = list(zip(times, distances))

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task, data)

    print(f"Part 1 Solution: {np.prod(results)}")


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        times = int("".join(f.readline().split(":")[1].strip().split()))
        distances = int("".join(f.readline().split(":")[1].strip().split()))

    data = (times, distances)

    results = task(data)

    print(f"Part 2 Solution: {results}")


if __name__ == "__main__":
    part_1()
    part_2()
