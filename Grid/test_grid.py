import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5, 5)

    def test_init(self):
        self.assertEqual(self.grid.width, 5)
        self.assertEqual(self.grid.height, 5)
        self.assertEqual(len(self.grid.grid), 5)
        self.assertEqual(len(self.grid.grid[0]), 5)
        self.assertEqual(self.grid.grid[0][0], " ")

    def test_display(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.grid.display()
            printed_output = mock_stdout.getvalue()
            expected_output = "|     |     |     |     |     |\n" \
                              "---------------------------------\n" \
                              "|     |     |     |     |     |\n" \
                              "---------------------------------\n" \
                              "|     |     |     |     |     |\n" \
                              "---------------------------------\n" \
                              "|     |     |     |     |     |\n" \
                              "---------------------------------\n" \
                              "|     |     |     |     |     |\n" \
                              "---------------------------------\n"
            self.assertEqual(printed_output, expected_output)

    def test_clear(self):
        self.grid.clear()
        for row in self.grid.grid:
            for cell in row:
                self.assertEqual(cell, " ")

if __name__ == '__main__':
    unittest.main()