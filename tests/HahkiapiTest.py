import unittest
from Hahkiapi import HahkiAPI
from GameGUI import GameGUI


class Test(unittest.TestCase):
    game = HahkiAPI()

    def test_how_kill(self):
        self.game.last_kill = "white"
        self.assertEqual(self.game.how_kill(), "white")
        self.game.last_kill = "black"
        self.assertEqual(self.game.how_kill(), "black")


if __name__ == '__main__':
    unittest.main()
