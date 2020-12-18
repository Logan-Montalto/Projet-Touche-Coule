from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
effectue = [False]
remplissage_tableau = []
player = []
tableau_adversaire = []


class GrilleAdversaire(App):
    """Classe représentant la grille de l'interface

            PRE: -
            POST: -
            """
    board = []

    def build(self):
        """Fonction d'affichage de l'interface

            PRE: -
            POST: -
            """

        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        self.title = player[0]
        self.grille = GridLayout(rows=11, cols=11)
        ordre = 0
        chiffre = 0
        lettre = 0
        for i in range(121):
            if i == 0:
                case = Button(text=' ', id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
            elif i < 11:
                case = Button(text=str(i - 1), id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
            elif i % 11 == 0:
                case = Button(text=str(list[ordre]), id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
                ordre += 1
            else:
                position = list[lettre] + str(chiffre)
                case = Button(text=str(position), id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
                chiffre += 1
                if chiffre == 10:
                    chiffre = 0
                    lettre += 1
        return self.grille

    def click(self, event):
        """Fonction qui détermine le click sur l'interface

                    PRE: -
                    POST: -
                    """
        remplissage_tableau.append(event.text)
        vrai_position = event.text
        a = vrai_position[0]
        for i in range(len(list)):
            if list[i] == vrai_position[0]:
                a = i
        if tableau_adversaire[int(a)][int(vrai_position[1])] != 0:
            event.text = "x"
        else:
            event.text = "o"
        effectue.append(True)

    def update(self):
        pass


def start():
    """Fonction qui démarre la grille

                PRE: -
                POST: -
                """
    GrilleAdversaire().run()
