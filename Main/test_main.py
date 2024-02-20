import unittest
from unittest.mock import patch
from main_game import MainGame

class TestMainGame(unittest.TestCase):
    @patch('Game.game.Game.run_turn', side_effect=[False, True])  # Mocking Game.run_turn
    def test_play(self, mock_run_turn):
        main_game = MainGame()
        with patch('builtins.print') as mock_print:
            main_game.play()
            mock_print.assert_called_with("Félicitations ! Le robot a atteint la cible en 1 étapes.")

if __name__ == '__main__':
    unittest.main()