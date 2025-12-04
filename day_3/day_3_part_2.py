from pathlib import Path


def highest_voltage(pack: str) -> int:
    split_pack = [num for num in pack]
    output = ""
    for i in range(12):
        if (i + -11) == 0:
            largest_jolt = max(split_pack)
        else:
            largest_jolt = max(split_pack[: i + -11])
        output += largest_jolt
        split_pack = split_pack[split_pack.index(largest_jolt) + 1 :]
    return int(output)


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    total = 0
    with p.open("r") as file:
        for line in file.readlines():
            total += highest_voltage(line.replace("\n", ""))
    print(total)
