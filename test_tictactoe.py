import unittest
from TTT import checkWin  # Import your functions from the main script

class TestTicTacToe(unittest.TestCase):
    def test_win_conditions(self):
        """Test winning conditions for X and O"""
        self.assertTrue(checkWin([["X", "X", "X"], [0, "O", 0], ["O", 0, "O"]]))
        self.assertTrue(checkWin([["O", "O", "O"], ["X", "X", 0], [0, "X", 0]]))

    def test_no_win(self):
        """Test for no win scenario"""
        self.assertFalse(checkWin([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))

if __name__ == "__main__":
    unittest.main()
