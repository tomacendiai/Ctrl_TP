# Ctrl_TP

test_grid.py :

    La classe de test TestGrid hérite de unittest.TestCase.
    La méthode setUp est utilisée pour initialiser une instance de la classe Grid avant chaque test.
    Trois tests sont définis :
        test_init: Vérifie que la grille est correctement initialisée avec la largeur, la hauteur et des espaces vides.
        test_display: Vérifie que la méthode display affiche correctement la grille.
        test_clear: Vérifie que la méthode clear réinitialise correctement la grille avec des espaces vides.

Notez l'utilisation de unittest.mock.patch pour simuler la sortie standard lors du test de la méthode display. Cela permet de capturer la sortie imprimée et de la comparer à la sortie attendue.
