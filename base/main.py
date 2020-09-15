from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sqlite3

from connected import Connected
from login import Login



class LoginApp(App):
    '''
    main class, it has ScreenManager with two widgets (login and connected widgets)
    and returning that manager
    '''
    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        #  manager.get_screen('connected').ids.wlc.text="aissa"
        return manager
if __name__ == "__main__":
    LoginApp().run()
