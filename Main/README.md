# Ctrl_TP

## Classe MainGame :

Cette classe est responsable de l'exécution du jeu. Elle crée une instance de la classe Game avec les paramètres spécifiés et lance la partie en utilisant une stratégie spécifiée. Voici comment elle fonctionne :

    __init__: Initialise le jeu en créant une grille, un robot, et une instance de la classe Game avec les paramètres spécifiés.
    play: Démarre la partie en exécutant les tours de jeu jusqu'à ce que la cible soit atteinte ou que le nombre maximal d'étapes soit dépassé. L'utilisateur peut spécifier la stratégie à utiliser.

## test_main.py :

    La classe de test TestMainGame hérite de unittest.TestCase.
    Le décorateur @patch est utilisé pour remplacer la méthode Game.game.Game.run_turn par une fonction de simulation qui renvoie successivement False puis True. Cela permet de contrôler le déroulement de la boucle dans la méthode play de la classe MainGame.
    Le test test_play vérifie que la méthode play de MainGame imprime le message approprié lorsque le jeu est terminé avec succès (lorsque la cible est atteinte).
    L'utilisation de patch('builtins.print') est pour intercepter l'appel à la fonction print et vérifier qu'elle est correcte. On utilise assert_called_with pour vérifier si la fonction print a été appelée avec le bon message.

Cet exemple illustre comment vous pouvez tester la classe MainGame en simulant le comportement de ses dépendances, telles que la classe Game, pour vérifier son bon fonctionnement dans différentes situations.

