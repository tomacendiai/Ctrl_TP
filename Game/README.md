# Ctrl_TP
##test_game.py
Ce code crée une classe de test TestGame qui hérite de unittest.TestCase. Trois tests sont définis :

    test_place_target: Ce test vérifie si la méthode place_target place correctement la cible sur la grille.

    test_check_collision: Ce test vérifie si la méthode check_collision retourne correctement True lorsque le robot se trouve sur la cible.

    test_run_turn: Ce test vérifie si la méthode run_turn met à jour le nombre d'étapes correctement et si elle termine correctement lorsque la cible est atteinte ou lorsque le nombre maximal d'étapes est atteint.

Dans ces tests, les appels aux fonctions random.randint et random.choice sont simulés à l'aide de la fonction patch pour garantir la reproductibilité des tests.
