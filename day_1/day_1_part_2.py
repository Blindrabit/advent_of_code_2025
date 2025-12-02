class Dail:
    def __init__(self, starting_position: int = 50):
        self._current_position = starting_position
        self._clicks = 0

    def turn_left(self, _input):
        """ if number has gone from position to negative and is smaller than -99"""
        value = (self._current_position - _input)
        if self._current_position > 0 > value or value == 0:
            self._clicks += 1
        if value <= -100:
            self._clicks += abs(value) // 100
        value = value % 100
        if value < 0:
            value = value + 100
        self._current_position = value

    def turn_right(self, _input):
        """if the number has gone from negative to positive and is larger than 99"""
        value = self._current_position + _input
        if self._current_position < 0 < value or value == 0:
            self._clicks += 1
        if value >= 100:
            self._clicks += value // 100

        self._current_position = value % 100

    def check_current_position(self):
        return self._current_position

    def get_clicks(self):
        return self._clicks


def crack_password(_turns: list[str]) -> int:
    dail = Dail()
    for turn in _turns:
        direction, _input = turn[0], int(turn[1:])
        if direction.upper() == "L":
            dail.turn_left(_input)
        elif direction.upper() == "R":
            dail.turn_right(_input)
    return dail.get_clicks()



if __name__ == "__main__":

    with open("../day_1/turns.txt", "r") as file:
        turns = []
        for line in file.readlines():
            turns.append(line.replace("\n", ""))

    print(crack_password(turns))