from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from Python.home import Screen_Home
from kivy.lang import Builder

Builder.load_file('telas/classe.kv')

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
        print("TelaForgotPassword inicializada")



if __name__ == '__main__':
    MyApp().run()