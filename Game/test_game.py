import unittest
from unittest.mock import patch
from game import Game
from Grid.grid import Grid
from Robot.robot import Robot

class TestGame(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5, 5)
        self.robot = Robot(1, 1)
        self.game = Game(self.grid, self.robot, max_steps=1000, show_grid=False)

    @patch('random.randint', side_effect=[2, 2])  # Mocking random.randint
    def test_place_target(self, mock_randint):
        self.game.place_target()
        self.assertEqual(self.game.target_x, 2)
        self.assertEqual(self.game.target_y, 2)
        self.assertEqual(self.game.grid.grid[2][2], "X")

    def test_check_collision(self):
        self.game.target_x = 1
        self.game.target_y = 1
        self.assertTrue(self.game.check_collision())

    @patch('random.choice', return_value='up')  # Mocking random.choice
    def test_run_turn(self, mock_choice):
        initial_steps = self.game.steps
        self.game.run_turn()
        self.assertEqual(self.game.steps, initial_steps + 1)
        self.assertTrue(self.game.target_reached or self.game.steps >= self.game.max_steps)

if __name__ == '__main__':
    unittest.main()