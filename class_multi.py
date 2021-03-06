class Multi:
    """Classe représentant le déroulement du jeu multi

            PRE: -
            POST: -
            """

    def __init__(self, tableau):
        """Fonction basée sur la création d'un tableau

        PRE: -
        POST: Récupère un tableau par l'appel de la classe
        """

        self.__tableau = tableau
        self.__jeu_fini = False

    def initialisation_jeu(self, pseudo, move):
        """Fonction d'initialisation du jeu

        PRE: Les conditions sont reprises dans le while
        POST: Renvoie un boolean
        """

        ok = False
        while True:
            if len(move) != 2 or move[0] < 'A' or 'K' <= move[0] < 'a' or 'k' <= move[0] or move[1] < '0' or move[
                1] > '9':
                print("Veuillez entrer une lettre et un chiffre")
                break
            else:
                print("Tu as joué", move[0].upper() + move[1])
                y = ord(move[0].upper()) - 65
                x = int(move[1])

                if 1 < self.__tableau[y][x] < 6:
                    print("Touché !")
                    if self.check():
                        print("Tu as gagné !")
                        ok = True
                        self.__jeu_fini = True
                        break
                else:
                    print("Raté !")
                self.__tableau[y][x] += 10
                ok = True
                break
        return ok

    def affichage_bateau(self):
        """Défini l'affichage de la grille avec les bateaux

        PRE: -
        POST: -
        """

        print()
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   0 1 2 3 4 5 6 7 8 9")
        for y in range(10):
            print(list[y], "|", end='')
            for x in range(10):
                if self.__tableau[y][x] == 10:
                    print('o', end='|')
                elif self.__tableau[y][x] % 10 == 0 and self.__tableau[y][x] != 0:
                    print('o', end='|')
                elif self.__tableau[y][x] > 10 and self.__tableau[y][x] % 10 != 0:
                    print('x', end='|')
                else:
                    print(str(self.__tableau[y][x]), end='|')
            print()

    def affichage_cache(self):
        """Défini l'affichage de la grille avec les bateaux cachés

        PRE: -
        POST: -
        """

        print()
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   0 1 2 3 4 5 6 7 8 9")
        for y in range(10):
            print(list[y], "|", end='')
            for x in range(10):
                if self.__tableau[y][x] == 10:
                    print('o', end='|')
                elif self.__tableau[y][x] % 10 == 0 and self.__tableau[y][x] != 0:
                    print('o', end='|')
                elif self.__tableau[y][x] > 10 and self.__tableau[y][x] % 10 != 0:
                    print('x', end='|')
                else:
                    print('.', end='|')
            print()

    def check(self):
        """Vérifie l'input de la fonction initialisation_jeu()

        PRE: -
        POST: Renvoie un boolean
        """

        compteur = 0
        for y in range(10):
            for x in range(10):
                if self.__tableau[y][x] > 10 and self.__tableau[y][x] % 10 != 0:
                    compteur += 1
        if compteur == 2:
            return True
        else:
            return False

    def winner(self):
        """Si renvoie True = partie s'arrête
        si renvoie False = partie continue
        par défaut = False

        PRE: -
        POST: Renvoie un boolean
        """
        return self.__jeu_fini
