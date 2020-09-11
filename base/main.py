from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from connected import Connected

class Login(Screen):
    def do_login(self, usr_text, pass_text):
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
            cred ={
                "aissa":"load",
                "mehdi":"loadT11"
            }
            if(app.username in cred and cred[app.username]== app.password):
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
        self.ids['usr'].text = ""
        self.ids['password'].text = ""




class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        return manager
    #  def get_application_config(self):
        #  if(not self.username):
            #  return super(LoginApp, self).get_application_config()
        #  conf_directory = os.path.join(self.user_data_dir ,self.username)
        #  if( not os.path.exists(conf_directory)):
            #  os.makedirs(conf_directory)
            #  return super(LoginApp,self).get_application_config(
                #  '{}/config.cfg'.format(conf_directory))

if __name__ == "__main__":
    LoginApp().run()
