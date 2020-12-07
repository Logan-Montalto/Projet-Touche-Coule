"""
Ce programme a été écrit par Liam Beaufils et Logan Montalto
Groupe de 2TL1-2
Cours de développement informatique II
"""

from donnees import creation_grille
import time
import keyboard
import interface
import threading

grille = creation_grille()
timer = []


"""Affichage de la grille"""

def affichage(g):
    print()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("   0 1 2 3 4 5 6 7 8 9")
    for y in range(10):
        print(list[y], "|", end='')
        for x in range(10):
            if g[y][x] == 10:
                print('o', end='|')
            elif g[y][x] % 10 == 0 and g[y][x] != 0:
                print('o', end='|')
            elif g[y][x] > 10 and g[y][x] % 10 != 0:
                print('x', end='|')
            else:
                print('.', end='|')
        print()


# Introdution au jeu
def init():
    nom = input("Saisir votre nom : ")
    print()
    print("Bienvenue", nom + '!')
    print("Le but est de couler les 4 bateaux le plus rapidement possible. Bonne Chance !")
    print()
    print("Tapez la touche 'Ctrl' pour commencer la partie : ")
    rk = keyboard.record(until='Ctrl')
    keyboard.play(rk, speed_factor=1)

    temps()

    touche = 0
    while touche != 2:
        affichage(grille)
        print()
        chaine = input("Quel est ton coup " + nom + ' ?')
        while len(chaine) != 2 or chaine[0] < 'A' or 'K' <= chaine[0] < 'a' or 'k' <= chaine[0] or chaine[1] < '0' or \
                chaine[1] > '9':
            print("Veuillez entrer une lettre et un chiffre")
            chaine = input("Quel est ton coup " + nom + ' ?')
        print("Tu as joué", chaine[0].upper() + chaine[1])
        y = ord(chaine[0].upper()) - 65
        x = int(chaine[1])

        if 1 < grille[y][x] < 6:
            print("Touché !")
            touche += 1
        else:
            print("Raté !")
        grille[y][x] += 10
    affichage(grille)
    print()


"""
Fonction commençant le timer (t1)
"""

def temps():
    t1 = time.time()
    timer.append(t1)


"""
Fontion de fin de jeu contenant le 2ème timer
Affiche le timer final 
timer final = (temps .time() au début du jeu) - (temps .time() au moment de la fin du jeu)
"""

def fin_jeu():
    print("Bien joué, tu as coulé tous les bateaux !")
    t2 = time.time()
    t = t2 - timer[0]
    z = round(t, 2)
    print("Tu as mis " + str(z) + " secondes.")


if __name__ == '__main__':
    thread_interface = threading.Thread(target=interface.start)
    thread_interface.start()
    init()
    affichage(grille)
    fin_jeu()