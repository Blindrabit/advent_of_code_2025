from pathlib import Path


def check_invalid(_id: str) -> bool:
    for n in range(1, (len(_id) // 2) + 1):
        options = [_id[i : i + n] for i in range(0, len(_id), n)]
        if len(set(options)) == 1:
            return True
    else:
        return False


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    with p.open("r") as file:
        for line in file.readlines():
            id_ranges = line.split(",")
    invalid_count = 0
    for id_range in id_ranges:
        for i in range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1):
            if check_invalid(str(i)):
                invalid_count += i

    print(invalid_count)
