import unittest
from X_O_Referee.MyAnswer import checkio

class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual("X",checkio(["X.O","XX.","XOO"]))

    def test_two(self):
        self.assertEqual('O',checkio(["OO.","XOX","XOX"]))

    def test_four(self):
        self.assertEqual("D",checkio(["OOX","XXO","OXX"]))

    def test_five(self):
        self.assertEqual("X",checkio(["O.X","XX.","XOO"]))

    def test_six(self):
        self.assertEqual("X",checkio(["XXX","O.O",".O."]))

    def test_seven(self):
        self.assertEqual("O",checkio(["...","XX.","OOO"]))


if __name__ == '__main__':
    unittest.main()
