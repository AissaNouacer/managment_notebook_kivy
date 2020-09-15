from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sqlite3

from connected import Connected
class Login(Screen):
    def do_login(self, usr_text, pass_text):
        '''
        do_login it's on_press botton to login fired, params taken from ids of the
        TextInput, basic controll of the fields must be filled with popup notification
        when all fields Ok, check the user and password if they are valid.
        '''
        app = App.get_running_app()

        app.username = usr_text
        app.password = pass_text
        if(not app.username and not app.password):
            info = "username and passowrd are required"
            self.ids.info.text=info
        elif(not app.username or not app.password):
            info = "username or passowrd are required!"
            self.ids.info.text=info


        else:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
#              c.execute('''
                     #  CREATE TABLE IF NOT EXISTS user (name text PRIMARY KEY, password text)
                     #  ''')

           #   c.execute('''
                     #  INSERT INTO user VALUES('aissa', 'load')
                     #  ''')
            #  conn.commit()
            #  user=[ele for ele in c.execute("select * from user where name='{}'".format(app.username))]
            c.execute("select * from user where name='{}'".format(app.username))
            user=c.fetchone()
            conn.close()
            if(user != None):
                cerds={
                    "name": user[0],
                    "password": user[1]
                    #  "name":"aissa",
                    #  "password":"load"
                }
                if(cerds["name"]!= app.username or cerds["password"]!= app.password):
                    info = "Invalid username or passowrd!"
                    self.ids.info.text=info
                else:
                    self.manager.transition = SlideTransition(direction="left")
                    self.manager.current = 'connected'
            else:
                info = "User doesn't exists !"
                self.ids.info.text=info




        #  app.config.read(app.get_application_config())
        #  app.config.write()
    def reset_form(self):
        '''
        reset_form cleaning the fields by calling it with self.ids[].text=""
        '''
        self.ids['usr'].text = ""
        self.ids['password'].text = ""



