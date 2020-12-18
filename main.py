"""
Ce programme a été écrit par Liam Beaufils et Logan Montalto
Groupe de 2TL1-2
Cours de développement informatique II
"""

import solo
import multijoueur


def start():
    """La fonction permet de choisir le mode de jeu avec un input

    :return: -
    """
    while True:
        mode = input("Quel mode voulez-vous faire ? (solo ou multi)")
        if mode == "solo":
            solo.welcome_player_console()
            break
        elif mode == "multi":
            multijoueur.choix_mode()
            break


if __name__ == '__main__':
    start()
