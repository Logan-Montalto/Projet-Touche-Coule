from random import randint
import keyboard


class Partie:
    def __init__(self):
        self.__grille = [[0] * 10 for i in range(10)]
        self.__debut_bateau_1 = randint(0, 9)
        self.__debut_bateau_2 = randint(0, 9)
        if randint(0, 1):  # booléen 0 pour faux et 1 pour vrai
            self.__debut_bateau_3, self.__debut_bateau_4 = 0, 1  # placement vertical
        else:
            self.__debut_bateau_3, self.__debut_bateau_4 = 1, 0  # placement horizontal

    def tirage_bateau(self):
        # coordonnées du début
        self.__debut_bateau_1 = randint(0, 9)
        self.__debut_bateau_2 = randint(0, 9)
        if randint(0, 1):  # booléen 0 pour faux et 1 pour vrai
            self.__debut_bateau_3, self.__debut_bateau_4 = 0, 1  # placement vertical
        else:
            self.__debut_bateau_3, self.__debut_bateau_4 = 1, 0  # placement horizontal
        return self.__debut_bateau_1, self.__debut_bateau_2, self.__debut_bateau_3, self.__debut_bateau_4

    def place_dispo(self, taille):
        print(taille)
        for i in range(taille):
            if self.__debut_bateau_1 < 10 and self.__debut_bateau_2 < 10:
                if 0 < self.__grille[self.__debut_bateau_2][self.__debut_bateau_1]:  # si il ya déjà un bateau
                    return False
                self.__debut_bateau_1 += self.__debut_bateau_3
                self.__debut_bateau_2 += self.__debut_bateau_4
            else:
                return False
        return True

    def place_bateau(self, taille):
        print(taille)
        for i in range(taille):
            self.__grille[self.__debut_bateau_2][self.__debut_bateau_1] = taille
            self.__debut_bateau_1 += self.__debut_bateau_3
            self.__debut_bateau_2 += self.__debut_bateau_4
        return self.__grille

    """
    Création d'une grille possédant 4 bateaux
    Les 4 bateaux ont des tailles sur la grilles dans une intervalle de 2 -> 6
    Les 4 bateaux ont donc une taille de 2, 3, 4 et 5 cases
    """

    def creation_grille(self):
        # tirages des bateaux
        for taille in range(2, 6):  # taille des bateaux de 2 à 5
            self.__debut_bateau_1, self.__debut_bateau_2, self.__debut_bateau_3, self.__debut_bateau_4 = self.tirage_bateau()
            while not self.place_dispo(taille):
                self.__debut_bateau_1, self.__debut_bateau_2, self.__debut_bateau_3, self.__debut_bateau_4 = self.tirage_bateau()
            self.__grille = self.place_bateau(taille)
        return self.__grille

    def deplacement(self):
        print(self.__grille)

game = Partie()
print(game.creation_grille())