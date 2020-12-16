class CreationGrillehuman:

    def __init__(self):
        self.__grille_human = [[0] * 10 for i in range(10)]
        self.__tableau_human = []
        self.__nombre_bateau = 0


    @property
    def grille(self):
        return self.__grille_human

    def placement(self, position_debut, position_fin, taille):
        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for i in range(len(liste)):
            if position_debut[0] == liste[i]:
                position_debut[0] = i
        for i in range(len(liste)):
            if position_fin[0] == liste[i]:
                position_fin[0] = i
        if not self.check(position_debut, position_debut, taille):
            return False
        else:
            a = position_debut[0]
            c = position_debut[1]
            if position_debut[0] == position_fin[0]:
                ajouter = "horizontal"
                if position_debut[1] > position_fin[1]:
                    a = position_fin[0]
                    c = position_fin[1]
            else:
                ajouter = "vertical"
                if position_debut[0] > position_fin[0]:
                    a = position_fin[0]
                    c = position_fin[1]

            self.__grille_human[position_debut[0]][position_debut[1]] = taille
            self.__grille_human[position_fin[0]][position_fin[1]] = taille
            ajout = taille - 1

            for i in range(1, ajout):
                if ajouter == "vertical":
                    self.__grille_human[a + i][c] = taille
                else:
                    self.__grille_human[a][c + i] = taille
            print(self.affichage())
            return True

    def check(self, position_debut, position_fin, taille):
        ok = True
        a = position_debut[0]
        c = position_debut[1]
        if a > 9 or c > 9 or position_fin[0] > 9 or position_fin[1] > 9:
            ok = False
        else:
            if position_debut[0] == position_fin[0]:
                ajouter = "horizontal"
                if position_debut[1] > position_fin[1]:
                    a = position_fin[0]
                    c = position_fin[1]
            else:
                ajouter = "vertical"
                if position_debut[0] > position_fin[0]:
                    a = position_fin[0]
                    c = position_fin[1]

            if self.__grille_human[position_debut[0]][position_debut[1]] != 0 or self.__grille_human[position_fin[0]][position_fin[1]] != 0:
                ok = False
            ajout = taille - 1

            for i in range(1, ajout):
                if ajouter == "vertical":
                    if self.__grille_human[a + i][c] != 0:
                        ok = False
                else:
                    if self.__grille_human[a][c + i] != 0:
                        ok = False
        return ok


    def affichage_grille(self):
        return self.__grille_human

    def affichage(self):
        print()
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   0 1 2 3 4 5 6 7 8 9")
        for y in range(10):
            print(list[y], "|", end='')
            for x in range(10):
                if self.__grille_human[y][x] == 10:
                    print('o', end='|')
                elif self.__grille_human[y][x] % 10 == 0 and self.__grille_human[y][x] != 0:
                    print('o', end='|')
                elif self.__grille_human[y][x] > 10 and self.__grille_human[y][x] % 10 != 0:
                    print('x', end='|')
                else:
                    print(str(self.__grille_human[y][x]), end='|')
            print()