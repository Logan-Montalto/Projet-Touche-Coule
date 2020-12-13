from random import randint
import keyboard
import time


class CreationTableau:
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

    """def place_dispo(self, taille):
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
                        return False"""

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
            """while self.place_dispo(taille):
                self.__x, self.__y, self.__debut_horizontal, self.__debut_vertical = self.tirage_bateau()"""
            self.__grille = self.place_bateau(taille)
        print(self.affichage())


    def affichage(self):
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
                    print('.', end='|')
            print()



class DeroulementJeuSolo:

    grille = creation_grille()
    timer = []

    def init(self):
        nom = input("Saisir votre nom : ")
        print()
        print("Bienvenue", nom + '!')
        print("Le but est de couler les 4 bateaux le plus rapidement possible. Bonne Chance !")
        print()
        print("Tapez la touche 'Ctrl' pour commencer la partie : ")
        rk = keyboard.record(until='Ctrl')
        keyboard.play(rk, speed_factor=1)

        self.temps()

        touche = 0
        while touche != 14:
            affichage(self.grille)
            print()
            chaine = input("Quel est ton coup " + nom + ' ?')
            while len(chaine) != 2 or chaine[0] < 'A' or 'K' <= chaine[0] < 'a' or 'k' <= chaine[0] or chaine[
                1] < '0' or \
                    chaine[1] > '9':
                print("Veuillez entrer une lettre et un chiffre")
                chaine = input("Quel est ton coup " + nom + ' ?')
            print("Tu as joué", chaine[0].upper() + chaine[1])
            y = ord(chaine[0].upper()) - 65
            x = int(chaine[1])

            if 1 < self.grille[y][x] < 6:
                print("Touché !")
                touche += 1
            else:
                print("Raté !")
            self.grille[y][x] += 10
        affichage(self.grille)
        print()

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



creation = CreationTableau
game = DeroulementJeuSolo

print(creation.creation_grille())
print(game)