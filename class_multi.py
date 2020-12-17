class Multi:
    """Class docstrings go here."""

    def __init__(self, tableau):
        """Class method docstrings go here."""

        self.__tableau = tableau
        self.__jeu_fini = False


    def initialisation_jeu(self, pseudo, move):
        """Class method docstrings go here."""

        # touche = 0
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
                        print("T'as gagné !")
                        ok = True
                        self.__jeu_fini = True
                        break
                    # touche += 1
                else:
                    print("Raté !")
                self.__tableau[y][x] += 10
                ok = True
                break
        return ok

    def affichage_bateau(self):
        """Class method docstrings go here."""

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
        """Class method docstrings go here."""

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
        """Class method docstrings go here."""

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
        return self.__jeu_fini
