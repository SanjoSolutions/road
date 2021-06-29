import unittest

from road import Road, row_a_has_connections_to_row_b


class TestRoad(unittest.TestCase):
    def test_request_state(self):
        road = Road()
        state = road.get_state()
        self.assertEqual(state, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0]
        ])


class TestRowAHasConnectionsToRowB(unittest.TestCase):
    def test_row_a_has_connections_to_row_b(self):
        row_a = [Road.EMPTY_SPACE, Road.OTHER_CAR, Road.OTHER_CAR, Road.OTHER_CAR]
        row_b = [Road.OTHER_CAR, Road.EMPTY_SPACE, Road.OTHER_CAR, Road.OTHER_CAR]
        self.assertTrue(row_a_has_connections_to_row_b(row_a, row_b))

    def test_row_a_has_connections_to_row_b2(self):
        row_a = [Road.EMPTY_SPACE, Road.OTHER_CAR, Road.OTHER_CAR, Road.EMPTY_SPACE]
        row_b = [Road.OTHER_CAR, Road.EMPTY_SPACE, Road.EMPTY_SPACE, Road.OTHER_CAR]
        self.assertTrue(row_a_has_connections_to_row_b(row_a, row_b))

    def test_row_a_has_connections_to_row_b_untrue(self):
        row_a = [Road.EMPTY_SPACE, Road.OTHER_CAR, Road.OTHER_CAR, Road.OTHER_CAR]
        row_b = [Road.OTHER_CAR, Road.OTHER_CAR, Road.EMPTY_SPACE, Road.OTHER_CAR]
        self.assertFalse(row_a_has_connections_to_row_b(row_a, row_b))
