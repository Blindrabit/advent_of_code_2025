from dataclasses import dataclass
from pathlib import Path


@dataclass
class PositionIndexes:
    row: int
    column: int


def count_surrounding_rolls(
    roll_matrix: list[list[str]], position: PositionIndexes
) -> int:
    if position.row > 0:
        forward_row = roll_matrix[position.row - 1]
    else:
        forward_row = []
    if position.row < len(roll_matrix) - 1:
        back_row = roll_matrix[position.row + 1]
    else:
        back_row = []

    if position.column > 0:
        left_index = position.column - 1
    else:
        left_index = position.column

    if position.column < len(matrix[0]) - 1:
        right_index = position.column + 2
    else:
        right_index = position.column + 1
    count = 0
    count += forward_row[left_index:right_index].count("@")
    count += roll_matrix[position.row][left_index:right_index].count("@") - 1
    count += back_row[left_index:right_index].count("@")

    if count < 4:
        return 1
    return 0


if __name__ == "__main__":

    p = Path(__file__).with_name("input.txt")
    matrix = []
    with p.open("r") as file:
        for line in file.readlines():
            matrix.append([_ for _ in line.replace("\n", "")])
    count = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if matrix[row_index][column_index] == "@":
                count += count_surrounding_rolls(
                    matrix, PositionIndexes(row_index, column_index)
                )

    print(count)
