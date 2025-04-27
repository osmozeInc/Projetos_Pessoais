from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


from Back_end.data_base import *

import webbrowser
import time

desfazer = 0

class Element_Reminder_FloatLayout_Class(FloatLayout):
    def __init__(self, lembretes, **kwargs):
        super(Element_Reminder_FloatLayout_Class, self).__init__(**kwargs)
        self.Manager = Reminder_Manager()

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
                              on_release=lambda instance: self.Manager.Abrir_link(lembretes[5])
                              ))
        
        self.add_widget(MDIconButton(icon="delete",
                                     size=("40dp", "40dp"),
                                     theme_text_color="Custom",
                                     text_color=(1, 1, 1, 1),
                                     pos_hint={'x': 0.975, 'center_y': 0.7},
                                     on_release=lambda instance: self.Notification(lembretes[0])
                                     ))
        
        self.add_widget(MDIconButton(icon="cog",
                                     size=("40dp", "40dp"),
                                     theme_text_color="Custom",
                                     text_color=(1, 1, 1, 1),
                                     pos_hint={'x': 0.975, 'center_y': 0.3},
                                     on_release=lambda instance: self.Manager.Editar_Lembrete(lembretes[0])
                                     ))
        
    def Notification(self, id):
        self.button_pressed = False

        card = MDCard(pos_hint={'center_x': 0.875,'center_y': 0.65})
        button = Button(text="Desfazer",
                        color=(1, 1, 1, 1),
                        background_color=[1, 0.25, 0.25, 0],
                        pos_hint={'center_x': 0.945, 'center_y': 0.65},
                        size_hint=(0.4, 0.3),
                        on_release=lambda instance: self.on_button_press(card, button))
        
        self.add_widget(card)
        self.add_widget(button)
        Clock.schedule_once(lambda dt: self.not_button_press(id, card, button), 4)
        
    def on_button_press(self, card, button):
            self.remove_widget(card)
            self.remove_widget(button)
            self.button_pressed = True

    def not_button_press(self, id, card, button):
        if self.button_pressed == False:
            self.Manager.Delete_Reminder(id)
            self.on_button_press(card, button)

class Reminder_Manager():
    def __init__(self):
        self.Update = Update_DB()
        self.Delete = Delete_DB()

    def Open_link(link):
        webbrowser.open(link)

    def Delete_Reminder(self, id):
        self.Delete.Delete_Reminder(id)

    def Not_Delete_Reminder(self):
        self.remove_widget(self.children[-1])
        

    def Edit_Reminder(self, id):
        pass
