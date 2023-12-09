import multiprocessing
from typing import List

CPU_COUNT = multiprocessing.cpu_count()


def task_p1(data: List[int]) -> int:
    differences = len(data) - 1

    data_matrix = [data]
    difference_list = [data[i + 1] - data[i] for i in range(differences)]
    data_matrix.append(difference_list)

    while not all(v == 0 for v in difference_list):
        differences = len(difference_list) - 1
        difference_list = [
            difference_list[i + 1] - difference_list[i] for i in range(differences)
        ]
        data_matrix.append(difference_list)

    for row in data_matrix[::-1]:
        if all(v == 0 for v in row):
            row += [0]
        else:
            row += [row[-1] + data_matrix[data_matrix.index(row) + 1][-1]]

    return data_matrix[0][-1]


def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = [list(map(int, data.strip().split())) for data in f.read().splitlines()]

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p1, data)

    print(f"Part 1 Solution: {sum(results)}")


def task_p2(data: List[int]) -> int:
    differences = len(data) - 1

    data_matrix = [data]
    difference_list = [data[i + 1] - data[i] for i in range(differences)]
    data_matrix.append(difference_list)

    while not all(v == 0 for v in difference_list):
        differences = len(difference_list) - 1
        difference_list = [
            difference_list[i + 1] - difference_list[i] for i in range(differences)
        ]
        data_matrix.append(difference_list)

    for row in data_matrix[::-1]:
        if all(v == 0 for v in row) and len(row) >= 1:
            # Python does not modify in place using =, only += does that like in part 1
            data_matrix[data_matrix.index(row)] = [0] + row
        else:
            data_matrix[data_matrix.index(row)] = [
                row[0] - data_matrix[data_matrix.index(row) + 1][0]
            ] + row

    return data_matrix[0][0]


def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = [list(map(int, data.strip().split())) for data in f.read().splitlines()]

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p2, data)

    print(f"Part 2 Solution: {sum(results)}")


if __name__ == "__main__":
    part_1()
    part_2()
