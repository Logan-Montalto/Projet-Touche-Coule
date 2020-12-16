import solo


def welcome_player_console():
    player = solo.DeroulementJeuSolo(input("Saisir votre nom : "))
    print(f"Bienvenue {player.pseudo} !")
    print(f"Le but est de couler les 4 bateaux le plus rapidement possible. Bonne Chance !")
    print()
    print(f"Tapez la touche 'Enter' pour commencer la partie : ")
    input()
    player.initialisation_jeu()

welcome_player_console()