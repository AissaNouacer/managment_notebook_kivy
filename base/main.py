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
            popup = Popup(title='Username & password',
                          content=Label(text=' Username & password not set'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            print("")
        elif(not app.username or not app.password):
            popup = Popup(title='Username or password',
                          content=Label(text='Username or password not set'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()


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
            if(user != None):
                cerds={
                    "name": user[0],
                    "password": user[1]
                    #  "name":"aissa",
                    #  "password":"load"
                }
                if(cerds["name"]== app.username and cerds["password"]== app.password):
                    self.manager.transition = SlideTransition(direction="left")
                    self.manager.current = 'connected'
            else:
                popup = Popup(title='creds not correct',
                              content=Label(text='Your username or password not correct'),
                              size_hint=(None, None), size=(400, 400))
                popup.open()



        #  app.config.read(app.get_application_config())
        #  app.config.write()
    def reset_form(self):
        '''
        reset_form cleaning the fields by calling it with self.ids[].text=""
        '''
        self.ids['usr'].text = ""
        self.ids['password'].text = ""




class LoginApp(App):
    '''
    main class, it has ScreenManager with two widgets (login and connected widgets)
    and returning that manager
    '''
    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        return manager
if __name__ == "__main__":
    LoginApp().run()
