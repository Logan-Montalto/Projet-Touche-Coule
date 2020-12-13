from random import randint
#import keyboard


class Partie:
    def __init__(self):
        self.__grille = [[0] * 10 for i in range(10)]


    def tirage_bateau(self):
        # coordonnées du début
        self.__y = randint(0, 9)
        self.__x = randint(0, 9)
        if randint(0, 1):  # booléen 0 pour faux et 1 pour vrai
            self.__debut_horizontal, self.__debut_vertical = 0, 1  # placement vertical
        else:
            self.__debut_horizontal, self.__debut_vertical = 1, 0  # placement horizontal
        return self.__x, self.__y, self.__debut_horizontal, self.__debut_vertical

    def place_dispo(self, taille):
        for i in range(taille):

            if self.__x < 10 and self.__y < 10:
                if 0 < self.__grille[self.__y][self.__x]:  # si il ya déjà un bateau
                    return True
                if self.__y + self.__debut_horizontal == 10 or self.__x + self.__debut_vertical == 10:
                    print("lol")
                    return True
                else:
                    self.__y += self.__debut_horizontal
                    self.__x += self.__debut_vertical
                    if 0 < self.__grille[self.__y][self.__x]:  # si il ya déjà un bateau
                        return True
                    if self.__y + self.__debut_horizontal == 10 or self.__x + self.__debut_vertical == 10:
                        print("lol")
                        return True
                    else:
                        return False





    def place_bateau(self, taille):
        for i in range(taille):
            self.__grille[self.__y][self.__x] = taille
            self.__y += self.__debut_horizontal
            self.__x += self.__debut_vertical
        return self.__grille

    """
    Création d'une grille possédant 4 bateaux
    Les 4 bateaux ont des tailles sur la grilles dans une intervalle de 2 -> 6
    Les 4 bateaux ont donc une taille de 2, 3, 4 et 5 cases
    """

    def creation_grille(self):
        # tirages des bateaux
        for taille in range(2, 6):  # taille des bateaux de 2 à 5
            self.__x, self.__y, self.__debut_horizontal, self.__debut_vertical = self.tirage_bateau()
            while self.place_dispo(taille):
                self.__x, self.__y, self.__debut_horizontal, self.__debut_vertical = self.tirage_bateau()
            self.__grille = self.place_bateau(taille)
        self.deplacement()

    def deplacement(self):
        print(self.__grille)

game = Partie()
print(game.creation_grille())