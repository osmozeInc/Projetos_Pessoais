from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from Python.home import Screen_Home
from kivy.lang import Builder
from Python.email_manager import *

Builder.load_file('telas/classe.kv')
Builder.load_file('telas/recuperar_senha.kv')

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_New_User(name='new_user'))
        sm.add_widget(Screen_Forgot_Password(name='forgot_password'))
        sm.add_widget(Screen_Home(name='home'))
        Window.size = (420, 800)
        return sm
    

class Screen_Login(Screen):
    pass

class Screen_New_User(Screen):
    pass

class Screen_Forgot_Password(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Enviar_Email_Recuperacao(self, email_client):
        ok = validar_email(email_client)
        if ok:
            Email_de_Recuperacao.Enviar_Email_Recuperacao(email_client)
        else:
            print('Email inválido')


        



if __name__ == '__main__':
    MyApp().run()