import regex as re
import multiprocessing

CPU_COUNT = multiprocessing.cpu_count()
INTS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
pattern = '|'.join(INTS)


def task_p1(data: str) -> int:
    i: int = 0
    j: int = len(data) - 1

    i_val: int = 0
    j_val: int = 0

    while i <= j:
        if data[i].isdigit():
            i_val = int(data[i])
            break
        i += 1

    while j >= i:
        if data[j].isdigit():
            j_val = int(data[j])
            break
        j -= 1

    return int(f"{i_val}{j_val}")


def part_1() -> None:
    with open("data_p1/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p1, data)

    with open("data_p1/data_output.txt", "w") as f:
        for i in range(len(results)):
            f.write(f"{data[i]} = {results[i]}\n")

    print(f"Part 1 Solution: {sum(results)}")


def task_p2(data: str) -> int:
    i: int = 0
    j: int = len(data) - 1

    i_val: int = 0
    j_val: int = 0
    
    while i <= j:

        if data[i].isdigit():
            i_val = int(data[i])
            break

        i_match = re.findall(pattern, data[i:], overlapped=True)
        if i_match:
            result = i_match[0]
            if data[i:i+len(result)] == result:     
                i_val = INTS.index(result) + 1
                break

        i += 1

    while j >= i:
        if data[j].isdigit():
            j_val = int(data[j])
            break

        j_match = re.findall(pattern, data[:j+1], overlapped=True)
        if j_match:
            result = j_match[-1]
            if data[j-len(result)+1:j+1] == result:
                j_val = INTS.index(result) + 1
                break
        j -= 1

    return int(f"{i_val}{j_val}")


def part_2() -> None:
    with open("data_p2/data.txt", "r") as f:
        data = f.read().splitlines()

    with multiprocessing.Pool(CPU_COUNT) as pool:
        results = pool.map(task_p2, data)

    with open("data_p2/data_output.txt", "w") as f:
        for i in range(len(results)):
            f.write(f"{data[i]} = {results[i]}\n")

    print(f"Part 2 Solution: {sum(results)}")


if __name__ == "__main__":
    part_1()
    part_2()
