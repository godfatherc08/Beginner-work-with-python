import kivy
from kivy.app import App
from kivy.uix.label import Label


kivy.require('2.2.1')


class my_app(App):
    def build(self):
        return Label(text="Hello World")


if __name__ == "__main__":
    my_app().run()
