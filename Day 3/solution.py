from typing import List, Tuple, Dict, DefaultDict


def task_p1(data: List[str]) -> int:
    rows, cols = len(data), len(data[0])
    symbols = {
        char for row in data for char in row if not char.isdigit() and char != "."
    }

    def is_valid_bbox(bbox: List[Tuple[int, int]]) -> bool:
        return any(
            data[y][x] in symbols for x, y in bbox if 0 <= y < rows and 0 <= x < cols
        )

    def find_digit_sequence(row: str, start: int) -> Tuple[int, int]:
        end = start
        while end < len(row) and row[end].isdigit():
            end += 1
        return start, end - 1

    def generate_bbox(x0: int, y0: int, x1: int, y1: int) -> List[Tuple[int, int]]:
        return [(x, y) for x in range(x0 - 1, x1 + 2) for y in [y0 - 1, y1 + 1]] + [
            (x, y) for y in range(y0, y1 + 1) for x in [x0 - 1, x1 + 1]
        ]

    total = 0
    for y, row in enumerate(data):
        x = 0
        while x < cols:
            if row[x].isdigit():
                start_x, end_x = find_digit_sequence(row, x)
                bbox = generate_bbox(start_x, y, end_x, y)
                if is_valid_bbox(bbox):
                    total += int(row[start_x : end_x + 1])
                x = end_x
            x += 1

    return total


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = f.read().splitlines()

    results = task_p1(data)

    print(f"Part 1 Solution: {results}")


def task_p2(data: List[str]) -> int:
    gears: Dict[Tuple[int, int], List[int]] = DefaultDict(list)

    rows, cols = len(data), len(data[0])

    def find_gears(part: int, bbox: List[Tuple[int, int]]) -> None:
        for x, y in bbox:
            if 0 <= y < rows and 0 <= x < cols:
                if data[y][x] == "*":
                    gears[(x, y)].append(part)

    def find_digit_sequence(row: str, start: int) -> Tuple[int, int]:
        end = start
        while end < len(row) and row[end].isdigit():
            end += 1
        return start, end - 1

    def generate_bbox(x0: int, y0: int, x1: int, y1: int) -> List[Tuple[int, int]]:
        return [(x, y) for x in range(x0 - 1, x1 + 2) for y in [y0 - 1, y1 + 1]] + [
            (x, y) for y in range(y0, y1 + 1) for x in [x0 - 1, x1 + 1]
        ]

    total = 0
    for y, row in enumerate(data):
        x = 0
        while x < cols:
            if row[x].isdigit():
                start_x, end_x = find_digit_sequence(row, x)
                x = end_x
                bbox = generate_bbox(start_x, y, end_x, y)
                part = int(row[start_x : end_x + 1])
                find_gears(part, bbox)
            x += 1

    for gear in gears:
        if len(gears[gear]) == 2:
            total += gears[gear][0] * gears[gear][1]

    return total


def part_2() -> None:
    with open("data/test_data.txt", "r") as f:
        data = f.read().splitlines()

    results = task_p2(data)

    print(f"Part 2 Solution: {results}")


if __name__ == "__main__":
    part_1()
    part_2()
