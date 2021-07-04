from enum import IntEnum
from itertools import product
from random import choice


class Action(IntEnum):
    MoveLeft = 0
    Stay = 1
    MoveRight = 2


class Road:
    NUMBER_OF_ROADS = 4
    NUMBER_OF_ROWS = 4
    EMPTY_SPACE = 0
    DRIVING_CAR = 1
    OTHER_CAR = 2

    def __init__(self):
        self.rows = None
        self.car_index = None
        self.reset()

    def reset(self):
        self.rows = [None] * Road.NUMBER_OF_ROWS
        for index in range(Road.NUMBER_OF_ROWS):
            self.rows[index] = [Road.EMPTY_SPACE] * Road.NUMBER_OF_ROADS
        self.car_index = 1
        return self.get_state()

    def step(self, action: Action):
        if action == Action.MoveLeft:
            self._move_left()
        elif action == Action.Stay:
            pass
        elif action == Action.MoveRight:
            self._move_right()
        self._next_step()
        done = self.is_game_over()
        reward = 0 if done else 1
        return self.get_state(), reward, done

    def _move_left(self):
        self.car_index = max(0, self.car_index - 1)

    def _move_right(self):
        self.car_index = min(self.car_index + 1, Road.NUMBER_OF_ROADS - 1)

    def _next_step(self):
        self.rows = self.rows[:-1]
        row = self._generate_row()
        self.rows.insert(0, row)

    def _generate_row(self):
        combinations = list(
            product(
                [Road.EMPTY_SPACE, Road.OTHER_CAR],
                repeat=Road.NUMBER_OF_ROADS
            )
        )
        combinations = combinations[:-1]
        combinations = [
            combination
            for combination
            in combinations
            if self._previous_row_has_connections_to_row(combination)
        ]
        return list(choice(combinations))

    def _previous_row_has_connections_to_row(self, row):
        previous_row = self.rows[0]
        return row_a_has_connections_to_row_b(previous_row, row)

    def get_state(self):
        state = self.rows
        state[-1] = state[-1].copy()
        state[-1][self.car_index] = Road.DRIVING_CAR
        return state

    def is_game_over(self):
        return self.rows[-1][self.car_index] == Road.OTHER_CAR


def row_a_has_connections_to_row_b(row_a, row_b):
    for index in range(Road.NUMBER_OF_ROADS):
        if row_a[index] == Road.EMPTY_SPACE:
            connected_empty_space = False
            for index2 in range(max(0, index - 1), min(index + 1, Road.NUMBER_OF_ROADS - 1) + 1):
                if row_b[index2] == Road.EMPTY_SPACE:
                    connected_empty_space = True
                    break
            if not connected_empty_space:
                return False
    return True


def print_state(state):
    for row in state:
        print(row)
