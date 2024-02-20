# Ctrl_TP

## Classe Game :

Cette classe est responsable de la logique du jeu. Elle prend en charge la création de la grille, la position du robot et de la cible, ainsi que la gestion des déplacements du robot en fonction de différentes stratégies. Voici une explication de ses fonctionnalités :

    __init__: Initialise la partie avec une grille, un robot, et d'autres paramètres comme le nombre maximal d'étapes et l'affichage de la grille.
    place_target: Place aléatoirement la cible sur la grille.
    check_collision: Vérifie si le robot a atteint la cible.
    random_movement: Choix aléatoire d'un mouvement parmi les directions disponibles.
    smart_movement: Calcul d'un mouvement intelligent basé sur la distance entre le robot et la cible.
    mixed_movement: Mélange de mouvements aléatoires et intelligents.
    run_turn: Exécute un tour de jeu en fonction de la stratégie choisie. Si aucune stratégie n'est spécifiée, elle utilise la stratégie aléatoire par défaut.


## test_game.py :

Ce code crée une classe de test TestGame qui hérite de unittest.TestCase. Trois tests sont définis :

    test_place_target: Ce test vérifie si la méthode place_target place correctement la cible sur la grille.

    test_check_collision: Ce test vérifie si la méthode check_collision retourne correctement True lorsque le robot se trouve sur la cible.

    test_run_turn: Ce test vérifie si la méthode run_turn met à jour le nombre d'étapes correctement et si elle termine correctement lorsque la cible est atteinte ou lorsque le nombre maximal d'étapes est atteint.

Dans ces tests, les appels aux fonctions random.randint et random.choice sont simulés à l'aide de la fonction patch pour garantir la reproductibilité des tests.
