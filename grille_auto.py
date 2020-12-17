from random import randint


class CreationTableauAuto:
    """Class docstrings go here."""

    def __init__(self):
        self.__grille = [[0] * 10 for i in range(10)]
        self.__tableau = []

    @property
    def grille(self):
        return self.__grille

    def tirage_bateau(self):
        """Class method docstrings go here."""

        # coordonnées du début

        self.__x = randint(0, 9)
        self.__y = randint(0, 9)
        if randint(0, 1):  # booléen 0 pour faux et 1 pour vrai
            self.__debut_horizontal, self.__debut_vertical = 0, 1  # placement vertical
        else:
            self.__debut_horizontal, self.__debut_vertical = 1, 0  # placement horizontal

    def place_bateau_tableau(self, taille):
        """Class method docstrings go here."""

        for i in range(taille):
            if i == 0:
                self.__tableau.append([self.__x, self.__y])
            else:
                self.__x += self.__debut_horizontal
                self.__y += self.__debut_vertical
                self.__tableau.append([self.__x, self.__y])

    def changement(self, ind):
        """Class method docstrings go here."""


        for u in ind:
            self.__tableau.pop(u)
        self.tirage_bateau()
        for i in range(len(ind)):
            if i == 0:
                self.__tableau.insert(ind[i], [self.__x, self.__y])
            else:
                self.__x += self.__debut_horizontal
                self.__y += self.__debut_vertical
                self.__tableau.insert(ind[i], [self.__x, self.__y])
        self.check()

    def check(self):
        erreur = []
        for i in range(len(self.__tableau)):
            for e in range(len(self.__tableau)):
                if self.__tableau[i] == self.__tableau[e] and i != e:
                    erreur.append(e)

        for i in erreur:
            y = 0
            x = 0
            z = 0
            v = 0
            if i < 2:
                print("bateau 1 erreur")
                if y == 0:
                    ind = [0, 1]
                    y += 1
                    self.changement(ind)
            if i < 5:
                print("bateau 2 erreur")
                if x == 0:
                    x += 1
                    ind = [2, 3, 4]
                    self.changement(ind)
            if i < 9:

                print("bateau 3 erreur")
                if z == 0:
                    z += 1
                    ind = [5, 6, 7, 8]
                    self.changement(ind)
            else:
                if v == 0:
                    v += 1
                    print("bateau 4 erreur")
                    ind = [9, 10, 11, 12, -1]
                    self.changement(ind)

        self.place_bateau_grille()

    def place_bateau_grille(self):
        """Class method docstrings go here."""

        compteur = 0
        for i in range(2, 6):
            taille = i
            for e in range(taille):
                self.__grille[self.__tableau[compteur][0]][self.__tableau[compteur][1]] = taille
                compteur += 1

    def creation_grille(self):
        """Class method docstrings go here."""

        # tirages des bateaux
        self.__tableau = []
        self.__grille = [[0] * 10 for i in range(10)]
        for taille in range(2, 6):  # taille des bateaux de 2 à 5
            self.tirage_bateau()
            self.place_bateau_tableau(taille)
        try:
            self.check()
        except IndexError:
            self.creation_grille()

    def affichage_grille(self):
        """Class method docstrings go here."""

        for i in self.__grille:
            print(i)

    def affichage(self):
        """Class method docstrings go here."""

        print()
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   0 1 2 3 4 5 6 7 8 9")
        for y in range(10):
            print(list[y], "|", end='')
            for x in range(10):
                if self.__grille[y][x] == 10:
                    print('o', end='|')
                elif self.__grille[y][x] % 10 == 0 and self.__grille[y][x] != 0:
                    print('o', end='|')
                elif self.__grille[y][x] > 10 and self.__grille[y][x] % 10 != 0:
                    print('x', end='|')
                else:
                    print(str(self.__grille[y][x]), end='|')
            print()

    def recup_grille(self):
        """Class method docstrings go here."""

        return self.__grille
