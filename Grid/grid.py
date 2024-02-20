#score : 6.36/10

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[" " for _ in range(width)] for _ in range(height)]

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * (4 * self.width - 1))

    def clear(self):
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
