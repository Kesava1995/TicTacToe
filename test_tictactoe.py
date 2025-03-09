import unittest
import tkinter as tk
from app import root, entries, printXO, clear_entries  # Import your GUI components

class TestTicTacToeGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up Tkinter main loop properly before tests."""
        cls.root = root
        cls.root.after(100, lambda: None)  # Prevent GUI from freezing
        cls.root.update_idletasks()
        cls.root.update()


    @classmethod
    def tearDownClass(cls):
        """Destroy the Tkinter instance after tests."""
        cls.root.destroy()

    def test_xo_insertion(self):
        """Test inserting 'X' and 'O' into the board."""
        global selected_entry  # Ensure we update the global variable

        entry = entries[0][0]  # Select top-left entry
        entry.event_generate("<Button-1>")  # Simulate mouse click
        selected_entry = entry  # Ensure printXO() has access
        entry.focus_set()  # Ensure entry is active

        printXO("X")
        self.assertEqual(entry.get(), "X", "Entry should contain 'X' after calling printXO")

        printXO("O")
        self.assertEqual(entry.get(), "O", "Entry should contain 'O' after calling printXO")




    def test_clear_entries(self):
        """Test clearing all entries in the grid."""
        entries[0][0].insert(0, "X")
        clear_entries()
        self.assertEqual(entries[0][0].get(), "")

if __name__ == "__main__":
    unittest.main()
