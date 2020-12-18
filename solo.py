import class_solo
import grille_auto


def welcome_player_console():
    """La fonction lance le déroulement du jeu solo

    :return: -
    """
    generation = grille_auto.CreationTableauAuto()
    generation.creation_grille()
    player = class_solo.DeroulementJeuSolo(input("Saisir votre nom : "), generation.recup_grille())
    print(f"Bienvenue {player.pseudo} !")
    print(f"Le but est de couler les 4 bateaux le plus rapidement possible. Bonne Chance !")
    print()
    print(f"Tapez la touche 'Enter' pour commencer la partie : ")
    input()
    player.initialisation_jeu()
