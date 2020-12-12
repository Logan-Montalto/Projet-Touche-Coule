from random import randint

"""affiche la grille g en argument"""


class Partie:
    def __init__(self, mode):
        self.__mode = mode


class joueur:
    def __init__(self, pseudo, score, temps):
        self.__pseudo = pseudo
        self.__score = score
        self.__temps = temps

class Grille:
    def __init__(self, case_vide, case_bateau, case_rate):
        self.__case_vide = case_vide
        self.__case_bateau = case_bateau
        self.__case_rate = case_rate


class Bateau:
    def __init__(self, nom, taille, x, y, est_coule):
        self.__nom = nom
        self.__taille = taille
        self.__x = x
        self.__y = y
        self.__est_coule = est_coule



def affichage(g):
    for y in range(10):
        print('|', end='')
        for x in range(10):
            print(g[y][x], end='|')
        print()


def tirage_bateau():
    # coordonnées du début
    debut_bateau_1 = randint(0, 9)
    debut_bateau_2 = randint(0, 9)
    if randint(0, 1):  # booléen 0 pour faux et 1 pour vrai
        debut_bateau_3, debut_bateau_4 = 0, 1  # placement vertical
    else:
        debut_bateau_3, debut_bateau_4 = 1, 0  # placement horizontal
    return debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4


def place_pour(g, taille, debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4):
    for i in range(taille):
        if debut_bateau_1 < 10 and debut_bateau_2 < 10:
            if 0 < g[debut_bateau_2][debut_bateau_1]:  # si il ya déjà un bateau
                return False
            debut_bateau_1 += debut_bateau_3
            debut_bateau_2 += debut_bateau_4
        else:
            return False
    return True


def place_bateau(g, t, debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4):
    for i in range(t):
        g[debut_bateau_2][debut_bateau_1] = t
        debut_bateau_1 += debut_bateau_3
        debut_bateau_2 += debut_bateau_4
    return g


"""
Création d'une grille possédant 4 bateaux
Les 4 bateaux ont des tailles sur la grilles dans une intervalle de 2 -> 6
Les 4 bateaux ont donc une taille de 2, 3, 4 et 5 cases
"""

def creation_grille():
    grille = [[0] * 10 for i in range(10)]
    # tirages des bateaux
    for taille in range(2, 6):  # taille des bateaux de 2 à 5
        debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4 = tirage_bateau()
        while not place_pour(grille, taille, debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4):
            debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4 = tirage_bateau()
        grille = place_bateau(grille, taille, debut_bateau_1, debut_bateau_2, debut_bateau_3, debut_bateau_4)
    return grille