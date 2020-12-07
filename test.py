import kivy
kivy.require('1.7.2')

from random import random
from random import choice
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_string("""
<Highest>:
    GridLayout:
        cols: 1
        Button:
            text: "Hi"
            on_press: root.new()
""")

class Highest(Screen):
    def new(self):
        self.background_color=(1.0, 0.0, 0.0, 1.0)


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Highest(name='Highest'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()