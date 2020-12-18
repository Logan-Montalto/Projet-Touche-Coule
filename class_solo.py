import time


class DeroulementJeuSolo:
    """Classe représentant le déroulement du jeu solo

        PRE: -
        POST: -
        """

    def __init__(self, pseudo, grille):
        """Fonction basée sur la création d'une grille et d'un pseudo

            PRE: -
            POST: Récupère le pseudo et la grille par l'appel de la classe
            """


        self.__pseudo = pseudo
        self.__grilles = grille

    @property
    def pseudo(self):
        return self.__pseudo

    def affichage_console(self):
        """Fonction d'affichage de la grille en console

            PRE: -
            POST: -
            """

        print()
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   0 1 2 3 4 5 6 7 8 9")
        for y in range(10):
            print(list[y], "|", end='')
            for x in range(10):
                if self.__grilles[y][x] == 10:
                    print('o', end='|')
                elif self.__grilles[y][x] % 10 == 0 and self.__grilles[y][x] != 0:
                    print('o', end='|')
                elif self.__grilles[y][x] > 10 and self.__grilles[y][x] % 10 != 0:
                    print('x', end='|')
                else:
                    print('.', end='|')
            print()


    def initialisation_jeu(self):
        """Fonction d'initialisation du jeu

            PRE: -
            POST: -
            """

        self.timer = []
        self.temps()

        touche = 0
        while touche != 14:
            self.affichage_console()
            print()
            chaine = input("Quel est ton coup " + self.__pseudo + ' ?')
            while len(chaine) != 2 or chaine[0] < 'A' or 'K' <= chaine[0] < 'a' or 'k' <= chaine[0] or chaine[
                1] < '0' or \
                    chaine[1] > '9':
                print("Veuillez entrer une lettre et un chiffre")
                chaine = input("Quel est ton coup " + self.__pseudo + ' ?')
            print("Tu as joué", chaine[0].upper() + chaine[1])
            y = ord(chaine[0].upper()) - 65
            x = int(chaine[1])

            if 1 < self.__grilles[y][x] < 6:
                print("Touché !")
                touche += 1
            else:
                print("Raté !")
            self.__grilles[y][x] += 10
        self.affichage_console()
        print()
        self.fin_jeu()


    def temps(self):
        """Fonction qui détermine le timer initial

            PRE: -
            POST: -
            """

        t1 = time.time()
        self.timer.append(t1)


    def fin_jeu(self):
        """Fonction qui termine le jeu, affichant le timer final

            PRE: -
            POST: -
            """

        print("Bien joué, tu as coulé tous les bateaux !")
        t2 = time.time()
        t = t2 - self.timer[0]
        z = round(t, 2)
        print("Tu as mis " + str(z) + " secondes.")
