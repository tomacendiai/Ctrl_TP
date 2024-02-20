from Grid.grid import Grid
from Robot.robot import Robot
from Game.game3 import Game

class MainGame:
    def __init__(
        self,
        grid_width=5,
        grid_height=5,
        robot_x=1,
        robot_y=1,
        max_steps=1000,
        show_grid=True,
    ):
        self.grid = Grid(grid_width, grid_height)
        self.robot = Robot(robot_x, robot_y)
        self.game = Game(
            self.grid, self.robot, max_steps=max_steps, show_grid=show_grid
        )

    def play(self, strategy="random"):  # Ajoutez un argument pour spécifier la stratégie
        while not self.game.run_turn(strategy=strategy):  # Passez la stratégie choisie à la méthode run_turn
            pass

        if self.game.target_reached:
            print(
                "Félicitations ! Le robot a atteint la cible en {} étapes.".format(
                    self.game.steps
                )
            )
        else:
            print(
                "Le robot n'a pas réussi à atteindre la cible dans le nombre maximum d'étapes."
            )

if __name__ == "__main__":
    main_game = MainGame()
    main_game.play(strategy="smart")  # Utilisation de la stratégie "smart"
