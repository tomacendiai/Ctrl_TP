# Ctrl_TP

test_robot.py :

    La classe de test TestRobot hérite de unittest.TestCase.
    La méthode setUp est utilisée pour initialiser une instance de la classe Robot avant chaque test.
    Huit tests sont définis pour les différentes méthodes de mouvement du robot (move_up, move_down, move_left, move_right), ainsi que pour tester les limites (bords) des déplacements lorsque le robot atteint le bord supérieur, inférieur, gauche ou droit de la grille.
    Chaque test utilise la méthode assertEqual pour vérifier si les coordonnées du robot sont correctement mises à jour après le mouvement.
