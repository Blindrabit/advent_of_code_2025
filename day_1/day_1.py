class Dail:
    def __init__(self):
        self._current_position: int = 50 # this is the dail start position

    def turn_left(self, _input):
        value = (self._current_position - _input) % 100
        if value < 0:
            value = value + 100
        self._current_position = value

    def turn_right(self, _input):
        self._current_position = (self._current_position + _input) % 100

    def check_current_position(self):
        return self._current_position

def crack_password(_turns: list[str]) -> int:
    dail = Dail()
    seen_zero = 0
    for turn in _turns:
        direction, _input = turn[0], int(turn[1:])
        if direction.upper() == "L":
            dail.turn_left(_input)
        elif direction.upper() == "R":
            dail.turn_right(_input)
        if dail.check_current_position() == 0:
            seen_zero += 1
    return seen_zero


if __name__ == "__main__":

    with open("day_1/turns.txt", "r") as file:
        turns = []
        for line in file.readlines():
            turns.append(line.replace("\n", ""))

    print(crack_password(turns))