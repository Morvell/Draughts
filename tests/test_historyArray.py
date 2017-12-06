import os
from unittest import TestCase
import unittest

import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))

from HistoryArray import HistoryArray


class TestHistoryArray(TestCase):
    def test_set_array(self):
        history = HistoryArray(2)
        history.put(((1, 1), (2, 2), (3)))
        print(history)
        historyTwo = HistoryArray(2)
        historyTwo.set_array("2@(1, 1)!(2, 2)!3+")
        self.assertEqual(str(historyTwo), str(history))

    def test_put(self):
        history = HistoryArray(2)
        history.put((1, 1))
        history.put((2, 2))
        history.put((3, 3))
        self.assertEqual(history.array[0], (2, 2))
        self.assertEqual(history.array[1], (3, 3))

    def test_get_last(self):
        history = HistoryArray(2)
        history.put((1, 1))
        history.put((2, 2))
        self.assertEqual(history.get_last(), (2, 2))

    def test_get_first(self):
        history = HistoryArray(2)
        history.put((1, 1))
        history.put((2, 2))
        self.assertEqual(history.get_first(0), 1)

    def test_get_second(self):
        history = HistoryArray(2)
        history.put((1, 1))
        history.put((2, 2))
        self.assertEqual(history.get_second(1), 2)

    def test_get_color(self):
        history = HistoryArray(2)
        history.put((1, 2))
        history.put((3, 4, 5))
        self.assertEqual(history.get_color(1), 5)

    def test_get_element(self):
        history = HistoryArray(2)
        history.put((1, 2))
        history.put((3, 4, 5))
        self.assertEqual(history.get_element(0), (1, 2))

    def test_str(self):
        history = HistoryArray(2)
        history.put((1, 2, 3))
        history.put((4, 5, 6))
        self.assertEqual(str(history), "2@1!2!3+4!5!6+")

    def test_len(self):
        history = HistoryArray(2)
        history.put((1, 2, 3))
        history.put((4, 5, 6))
        self.assertEqual(len(history), 2)


if __name__ == '__main__':
    unittest.main()