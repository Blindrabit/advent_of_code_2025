from pathlib import Path


def highest_voltage(pack: str) -> int:
    # create list of highest number indexes then create index +1 for next highest and
    split_pack = [num for num in pack]
    max_first = max(split_pack[:-1])
    max_second = max(split_pack[split_pack.index(max_first) + 1 :])
    return int(max_first + max_second)


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    total = 0
    with p.open("r") as file:
        for line in file.readlines():
            total += highest_voltage(line.replace("\n", ""))
    print(total)
