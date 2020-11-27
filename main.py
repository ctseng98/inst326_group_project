import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

# class in which we are creating the button
Config.set("graphics", "resizable", 1)


class Digit_input(GridLayout):
    pass


class FortuneApp(App):
    def build(self):
        return Digit_input()


# creating object and running it

FortuneApp().run()