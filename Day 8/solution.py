from math import lcm
from typing import Dict, Any

def task_p1(path: str, nodes: Dict[str, Any]) -> int:
    count = 0
    current = 'AAA'

    while current != 'ZZZ':
        direction = path[count % len(path)]
        if direction == 'R':
            current = nodes[current][1]
        elif direction == 'L':
            current = nodes[current][0]
        count += 1

    return count


def part_1() -> None:
    with open("data_p1/data.txt", "r") as f:
        path = f.readline().strip()
        f.readline()
        nodes = {i.split(" = ")[0]:[i.split(" = ")[1].replace("(", "").split(",")[0], i.split(" = ")[1].replace(")", "").split(", ")[1]] for i in f.read().splitlines()}
    
    result = task_p1(path, nodes)

    print(f"Part 1 Solution: {result}")


def task_p2(path: str, nodes: Dict[str, Any]) -> int:
    count = 0
    current = [node for node in nodes.keys() if node[-1] == 'A']
    
    solutions = []
    for node in current:
        count = 0
        while node[-1] != 'Z':
            direction = path[count % len(path)]
            if direction == 'R':
                node = nodes[node][1]
            elif direction == 'L':
                node = nodes[node][0]
            count += 1
        solutions.append(count)

    return lcm(*solutions)


def part_2() -> None:
    with open("data_p2/data.txt", "r") as f:
        path = f.readline().strip()
        f.readline()
        nodes = {i.split(" = ")[0]:[i.split(" = ")[1].replace("(", "").split(",")[0], i.split(" = ")[1].replace(")", "").split(", ")[1]] for i in f.read().splitlines()}
    
    result = task_p2(path, nodes)

    print(f"Part 2 Solution: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
