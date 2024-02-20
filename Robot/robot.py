#score : 5.62/10

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, grid_height):
        if self.y > 0:
            self.y -= 1

    def move_down(self, grid_height):
        if self.y < grid_height - 1:
            self.y += 1

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self, grid_width):
        if self.x < grid_width - 1:
            self.x += 1
