from pathlib import Path


def check_invalid(_id: int) -> bool:
    str_id = str(_id)
    return str_id[: len(str_id) // 2] == str_id[len(str_id) // 2 :]


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    with p.open("r") as file:
        turns = []
        for line in file.readlines():
            id_ranges = line.split(",")
    invalid_count = 0
    for id_range in id_ranges:
        for i in range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1):
            if check_invalid(i):
                invalid_count += i

    print(invalid_count)
