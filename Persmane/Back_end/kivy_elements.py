from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser

from Back_end.data_base import *


class Element_FloatLayout_Class(FloatLayout):
    def __init__(self, lembretes, **kwargs):
        super(Element_FloatLayout_Class, self).__init__(**kwargs)
        self.Manager = Element_Manager()

        # print(lembretes[0])   id do lembrete (chave primaria)
        # print(lembretes[1])   Titulo do lembrete
        # print(lembretes[2])   Data do lembrete
        # print(lembretes[3])   Hora do lembrete
        # print(lembretes[4])   Descrição do lembrete
        # print(lembretes[5])   Link do lembrete

        descricao = lembretes[4]
        if len(descricao) > 100:
            descricao = descricao[:100] + '\n' + descricao[100:]

        self.add_widget(Label(text=lembretes[1],
                              font_size=28,
                              pos_hint={'x': -0.4, 'center_y': 0.8}))
        
        self.add_widget(Label(text=f"{lembretes[2]} - {lembretes[3]}",
                              font_size=28,
                              pos_hint={'x': 0.35, 'center_y': 0.8}))
        
        self.add_widget(Label(text=f"{descricao}",
                              font_size=20,
                              halign='left',
                              color=(0.5, 0.5, 0.5, 1),
                              text_size=(self.width * 12, None),
                              pos_hint={'x': -0.1,'center_y': 0.4},
                              ))
        
        self.add_widget(Button(text=f"Link da tarefa",
                              font_size=20,
                              halign='left',
                              color=(0.5, 0.5, 0.5, 1),
                              background_color=(0.5, 0.5, 0.5, 0),
                              size_hint=(None, None),
                              size=(130, 30),
                              pos_hint={'x': 0.8,'center_y': 0.4},
                              on_release=lambda instance: Abrir_link(lembretes[5])
                              ))
        
        self.add_widget(MDIconButton(icon="delete",
                                     icon_size="30sp",
                                     theme_text_color="Custom",
                                     text_color=(1, 1, 1, 1),
                                     pos_hint={'x': 0.975, 'center_y': 0.7},
                                     on_release=lambda instance: self.Manager.Delete_Lembrete(lembretes[0])
                                     ))
        
        self.add_widget(MDIconButton(icon="cog",
                                     icon_size="30sp",
                                     theme_text_color="Custom",
                                     text_color=(1, 1, 1, 1),
                                     pos_hint={'x': 0.975, 'center_y': 0.3},
                                     on_release=lambda instance: self.Manager.Editar_Lembrete(lembretes[0])
                                     ))


class Element_Manager(Screen):
    def __init__(self):
        from main import Update_Screen
        self.Update = Update_DB()
        self.Delete = Delete_DB()

    def Abrir_link(link):
        webbrowser.open(link)

    def Delete_Lembrete(self, id):
        self.Delete.Delete_Reminder(id)
        
        
    def Editar_Lembrete(self, id):
        pass
