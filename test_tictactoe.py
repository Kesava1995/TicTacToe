import unittest
import tkinter as tk
from app import root, printXO, entries, clear_entries, status_label

class TestTicTacToeGUI(unittest.TestCase):

    def setUp(self):
        """Initialize Tkinter root before each test."""
        self.root = root

    def test_initial_ui(self):
        """Check if UI elements exist initially."""
        self.assertIsNotNone(entries)  # Ensure grid entries exist
        self.assertIsNotNone(status_label)  # Ensure status label exists

    def test_xo_insertion(self):
        """Test inserting 'X' and 'O' into the board."""
        # Select an entry (mimic user click)
        selected_entry = entries[0][0]
        selected_entry.focus_set()  # Simulate selecting the entry
        
        # Insert 'X'
        printXO("X")
        self.assertEqual(selected_entry.get(), "X")

        # Insert 'O'
        selected_entry.delete(0, tk.END)
        printXO("O")
        self.assertEqual(selected_entry.get(), "O")

    def test_clear_entries(self):
        """Test clearing all entries in the grid."""
        entries[0][0].insert(0, "X")
        entries[1][1].insert(0, "O")
        clear_entries()
        
        for row in entries:
            for entry in row:
                self.assertEqual(entry.get(), "")

if __name__ == "__main__":
    unittest.main()
