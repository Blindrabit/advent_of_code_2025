from dataclasses import dataclass
from pathlib import Path


@dataclass
class IdRange:
    lower_bound: int
    upper_bound: int


def find_all_fresh_ingredient_ids(_fresh_id_ranges):
    _fresh_id_ranges = [
        IdRange(lower_bound=int(r[0]), upper_bound=int(r[1])) for r in _fresh_id_ranges
    ]

    _fresh_id_ranges.sort(key=lambda x: x.lower_bound)

    # so brute force doesn't work lets consider a smarter options
    # as we know 10-14 and 12-18 and 16-20 can be reduced to 10-20
    # lets first reduce the ranges first then we can 20-10 + 1

    # so taking the test data check if lower or upper bound falls between range already
    # if it does we can drop that and extend the upper or lower bound of the existing
    # range if the other value is higher or lower
    # then we can repeat it until the it can not be reduced anymore

    reduced = True
    while reduced:
        reduced = False
        for i in range(len(_fresh_id_ranges)):
            for _i, _range in enumerate(_fresh_id_ranges):
                if _i == i:
                    continue
                elif (
                    _range.lower_bound
                    <= _fresh_id_ranges[i].lower_bound
                    <= _range.upper_bound
                ):
                    if _range.upper_bound < _fresh_id_ranges[i].upper_bound:
                        _range.upper_bound = _fresh_id_ranges[i].upper_bound
                        reduced = True
                        break
                elif (
                    _range.lower_bound
                    <= _fresh_id_ranges[i].upper_bound
                    <= _range.upper_bound
                ):
                    if _range.lower_bound > _fresh_id_ranges[i].lower_bound:
                        _range.lower_bound = _fresh_id_ranges[i].lower_bound
                        reduced = True
                        break
                # elif

        new_ranges = []
        # this is to remove duplicates
        for _range in _fresh_id_ranges:
            if _range not in new_ranges:
                new_ranges.append(_range)
        _fresh_id_ranges = new_ranges

    count = 0
    higher = 0
    for _range in _fresh_id_ranges:
        # doesn't count ranges which fall inside another range
        if not _range.lower_bound > higher:
            continue
        higher = _range.upper_bound
        count += _range.upper_bound - _range.lower_bound + 1
    return count


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    fresh_id_ranges = []
    with p.open("r") as file:
        for line in file.readlines():
            if line.__contains__("-"):
                fresh_id_ranges.append(line.replace("\n", "").split("-"))

    print(find_all_fresh_ingredient_ids(fresh_id_ranges))
