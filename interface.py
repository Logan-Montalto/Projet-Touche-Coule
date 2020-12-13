from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

class GrilleAdversaire(App):

    board = []

    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        self.title = 'Touché-Coulé'
        self.grille = GridLayout(rows=11, cols=11)
        ordre = 0
        for i in range(121):
            if i == 0:
                case = Button(text=' ', id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
            elif i < 11:
                case = Button(text=str(i), id=str(i))
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
                case = Button(text=' ', id=str(i))
                self.grille.add_widget(case)
                case.bind(on_press=self.click)
                self.board.append(case)
        return self.grille

    def click(self, event):
        for i in range(121):
            if self.board[i].id == event.id:
                print(event.id)
                event.background = 'blue'


    def update(self):
        pass


def start():
    GrilleAdversaire().run()
