import operator
from dataclasses import dataclass
from functools import reduce
from pathlib import Path


@dataclass
class CalculationObject:
    value_list: list
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
    lines = []
    with p.open("r") as file:
        for line in file.readlines():
            lines.append(list(reversed(" " + line.replace("\n", ""))))

    last_line = lines.pop(-1)

    value_lists = []
    _operator = ""
    obj = CalculationObject([])
    for i in range(len(lines[0])):
        if all([True if line[i] == " " else False for line in lines]):
            obj.operation = _operator
            value_lists.append(obj)
            obj = CalculationObject([])
        else:
            obj.value_list.append(int("".join([line[i] for line in lines])))
        if last_line[i] in ["+", "*"]:
            _operator = last_line[i]
    calculator = Calculator()
    total = 0
    for obj in value_lists:
        if obj.operation == "*":
            total += calculator.multiply_list(obj.value_list)
        elif obj.operation == "+":
            total += calculator.sum_list(obj.value_list)

    print(total)
