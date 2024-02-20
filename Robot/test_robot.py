import unittest
from robot import Robot 

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(3, 3)

    def test_move_up(self):
        self.robot.move_up(5)
        self.assertEqual(self.robot.y, 2)

    def test_move_up_boundary(self):
        self.robot.move_up(1)
        self.assertEqual(self.robot.y, 0)

    def test_move_down(self):
        self.robot.move_down(5)
        self.assertEqual(self.robot.y, 4)

    def test_move_down_boundary(self):
        self.robot.move_down(5)
        self.assertEqual(self.robot.y, 4)

    def test_move_left(self):
        self.robot.move_left()
        self.assertEqual(self.robot.x, 2)

    def test_move_left_boundary(self):
        self.robot.move_left()
        self.assertEqual(self.robot.x, 2)

    def test_move_right(self):
        self.robot.move_right(5)
        self.assertEqual(self.robot.x, 4)

    def test_move_right_boundary(self):
        self.robot.move_right(1)
        self.assertEqual(self.robot.x, 0)

if __name__ == '__main__':
    unittest.main()