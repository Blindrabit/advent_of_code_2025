from pathlib import Path


def check_for_fresh_ingredients(_fresh_id_ranges, _inventory_ids):
    count = 0
    _fresh_id_ranges = [(int(r[0]), int(r[1])) for r in _fresh_id_ranges]
    for _id in _inventory_ids:
        if any([True for r in _fresh_id_ranges if r[0] <= _id <= r[1]]):
            count += 1
    return count


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    fresh_id_ranges = []
    inventory_ids = []
    with p.open("r") as file:
        for line in file.readlines():
            if line == "\n":
                continue
            elif line.__contains__("-"):
                fresh_id_ranges.append(line.replace("\n", "").split("-"))
            else:
                inventory_ids.append(int(line.replace("\n", "")))
    print(check_for_fresh_ingredients(fresh_id_ranges, inventory_ids))
