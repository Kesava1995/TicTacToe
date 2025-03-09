import unittest
import tkinter as tk
from TicTacToe import YourAppClass  # Import your Tkinter class

class TestTkinterApp(unittest.TestCase):
    def setUp(self):
        """Initialize Tkinter before each test."""
        self.root = tk.Tk()
        self.app = YourAppClass(self.root)

    def tearDown(self):
        """Close Tkinter GUI after test execution."""
        self.root.destroy()  # Close the GUI to prevent hanging

    def test_ui_element(self):
        """Check if UI elements exist."""
        self.assertIsNotNone(self.app.some_widget)  # Example check

if __name__ == "__main__":
    unittest.main()
