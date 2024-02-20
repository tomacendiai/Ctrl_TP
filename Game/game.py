#score : 7.95/10

from Grid.grid import Grid
from Robot.robot import Robot
import random


class Game:
    def __init__(self, grid, robot, max_steps=1000, show_grid=False):
        self.grid = grid
        self.robot = robot
        self.show_grid = show_grid
        self.max_steps = max_steps
        self.steps = 0  # Nombre d'�tapes pour atteindre la cible
        self.place_target()
        self.target_reached = False

    def place_target(self):
        self.target_x = random.randint(0, self.grid.width - 1)
        self.target_y = random.randint(0, self.grid.height - 1)
        self.grid.grid[self.target_y][
            self.target_x
        ] = "X"  # Marquer la cible dans la grille

    def check_collision(self):
        if self.robot.x == self.target_x and self.robot.y == self.target_y:
            return True
        return False

    def run_turn(self):
        # V�rifier si la cible a d�j� �t� atteinte
        if self.target_reached:
            return True

        # V�rifier si le nombre d'�tapes a d�pass� la limite
        if self.steps >= self.max_steps:
            return False

        # D�placement du robot
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            self.robot.move_up(self.grid.height)
        elif direction == "down":
            self.robot.move_down(self.grid.height)
        elif direction == "left":
            self.robot.move_left()
        elif direction == "right":
            self.robot.move_right(self.grid.width)

        # Affichage de la grille apr�s le d�placement du robot
        if self.show_grid:
            self.grid.clear()
            self.grid.grid[self.robot.y][self.robot.x] = "R"
            self.grid.grid[self.target_y][self.target_x] = "X"
            self.grid.display()

        # V�rification si le robot touche la cible
        self.steps += 1
        if self.check_collision():
            self.target_reached = True
            return True
        return False
