import operator
from dataclasses import dataclass
from functools import reduce
from pathlib import Path


@dataclass
class CalculationObject:
    value_list: list[int]
    operation: str | None = None


class Calculator:
    @staticmethod
    def sum_list(values: list[int]) -> int:
        return sum(values)

    @staticmethod
    def multiply_list(values: list[int]) -> int:
        return reduce(operator.mul, values, 1)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    with p.open("r") as file:
        value_lists = []
        first_line = filter(("").__ne__, file.readline().replace("\n", "").split(" "))
        for num in first_line:
            value_lists.append(CalculationObject([int(num)]))

        for line in file.readlines():
            for index, num in enumerate(
                list(filter(("").__ne__, line.replace("\n", "").split(" ")))
            ):
                if num in ["+", "*"]:
                    value_lists[index].operation = num
                else:
                    value_lists[index].value_list.append(int(num))
    calculator = Calculator()
    total = 0
    for obj in value_lists:
        if obj.operation == "*":
            total += calculator.multiply_list(obj.value_list)
        elif obj.operation == "+":
            total += calculator.sum_list(obj.value_list)

    print(total)
