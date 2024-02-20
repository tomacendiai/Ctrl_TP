from Grid.grid import Grid
from Robot.robot import Robot
import random

class Game:
    def __init__(self, grid, robot, max_steps=1000, show_grid=False):
        self.grid = grid
        self.robot = robot
        self.show_grid = show_grid
        self.max_steps = max_steps
        self.steps = 0
        self.place_target()
        self.target_reached = False

    def place_target(self):
        self.target_x = random.randint(0, self.grid.width - 1)
        self.target_y = random.randint(0, self.grid.height - 1)
        self.grid.grid[self.target_y][self.target_x] = "X"

    def check_collision(self):
        if self.robot.x == self.target_x and self.robot.y == self.target_y:
            return True
        return False

    def random_movement(self):
        return random.choice(["up", "down", "left", "right"])

    def smart_movement(self):
        # Calculer la distance entre le robot et la cible
        distance_x = abs(self.robot.x - self.target_x)
        distance_y = abs(self.robot.y - self.target_y)

        # Choisir le mouvement en fonction de la distance
        if distance_x > distance_y:
            if self.robot.x < self.target_x:
                return "right"
            else:
                return "left"
        else:
            if self.robot.y < self.target_y:
                return "down"
            else:
                return "up"
    
    def mixed_movement(self):
        if random.random() < 0.5:
            return self.smart_movement()
        else:
            return self.random_movement()
    

    def run_turn(self, strategy="random"):
        if self.target_reached:
            return True

        if self.steps >= self.max_steps:
            return False

        if strategy == "random":
            direction = self.random_movement()
        elif strategy == "smart":
            direction = self.smart_movement()
        elif strategy == "mixed":
            direction = self.mixed_movement()
        else:
            raise ValueError("Invalid strategy")

        if direction == "up":
            self.robot.move_up(self.grid.height)
        elif direction == "down":
            self.robot.move_down(self.grid.height)
        elif direction == "left":
            self.robot.move_left()
        elif direction == "right":
            self.robot.move_right(self.grid.width)

        if self.show_grid:
            self.grid.clear()
            self.grid.grid[self.robot.y][self.robot.x] = "R"
            self.grid.grid[self.target_y][self.target_x] = "X"
            self.grid.display()

        self.steps += 1
        if self.check_collision():
            self.target_reached = True
            return True
        return False
