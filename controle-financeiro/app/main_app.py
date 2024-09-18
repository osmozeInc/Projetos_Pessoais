from kivy.app import App # type: ignore
from kivy.uix.screenmanager import ScreenManager # type: ignore
from app.screens.tela_principal import HomeScreen


class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))

        self.sm.current = 'home'
        self.load_kv('../resources/kv/main.kv')
        return self.sm
