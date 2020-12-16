import time


class DeroulementJeuSolo:

    def __init__(self, pseudo):
        """

                PRE : ?
                POST : ?
                """

        self.__pseudo = pseudo
        self.__grilles = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    @property
    def pseudo(self):
        return self.__pseudo

    """Fonction d'affichage de la grille de jeu du mode solo"""

    def affichage_console(self):
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

    """Fontion d'initialisation du jeu lançant le timer du mode solo"""

    def initialisation_jeu(self):

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

    """
    Fonction commençant le timer (t1)
    """

    def temps(self):
        t1 = time.time()
        self.timer.append(t1)

    """
    Fontion de fin de jeu contenant le 2ème timer
    Affiche le timer final 
    timer final = (temps .time() au début du jeu) - (temps .time() au moment de la fin du jeu)
    """

    def fin_jeu(self):
        print("Bien joué, tu as coulé tous les bateaux !")
        t2 = time.time()
        t = t2 - self.timer[0]
        z = round(t, 2)
        print("Tu as mis " + str(z) + " secondes.")