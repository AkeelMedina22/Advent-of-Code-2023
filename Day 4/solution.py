import multiprocessing
from typing import List

CPU_COUNT = multiprocessing.cpu_count()


def task_p1(data: str) -> int:
    target: List[int] = list(
        map(
            int,
            data.split(" | ")[0].split(":")[1].strip().replace("  ", " ").split(" "),
        )
    )
    current: List[int] = list(
        map(int, data.split(" | ")[1].strip().replace("  ", " ").split(" "))
    )

    def total(length: int) -> int:
        result = int(length > 0)
        for i in range(length - 1):
            result *= 2
        return result

    matching = list(filter(lambda x: x in current, target))

    return total(len(matching))


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p1, data)

    print(f"Part 1 Solution: {sum(results)}")


def task_p2_1(data: str) -> int:
    target: List[int] = list(
        map(
            int,
            data.split(" | ")[0].split(":")[1].strip().replace("  ", " ").split(" "),
        )
    )
    current: List[int] = list(
        map(int, data.split(" | ")[1].strip().replace("  ", " ").split(" "))
    )

    matching = list(filter(lambda x: x in current, target))

    return len(matching)

def task_p2_2(data: List[int]) -> List[int]:
    
    cards = dict(enumerate(data, start=1))
    results = dict([(i, 1) for i in range(1, len(cards) + 1)])
    
    for i in range(1, len(cards)+1):
        matching = cards[i]
        for j in range(i+1, i+1+matching):
            results[j] += 1 * results[i]

    return list(results.values())


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p2_1, data)

    results = task_p2_2(results)

    print(f"Part 2 Solution: {sum(results)}")


if __name__ == "__main__":
    part_1()
    part_2()
