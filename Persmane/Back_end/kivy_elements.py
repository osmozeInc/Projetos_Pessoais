from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Element_FloatLayout_Class(FloatLayout):
    def __init__(self, lembretes, **kwargs):
        super(Element_FloatLayout_Class, self).__init__(**kwargs)

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
                              pos_hint={'x': 0.4, 'center_y': 0.8}))
        
        self.add_widget(Label(text=f"{descricao}",
                              font_size=20,
                              halign='left',
                              color=(0.5, 0.5, 0.5, 1),
                              text_size=(self.width * 12, None),
                              pos_hint={'x': -0.1,'center_y': 0.4},
                              ))
        
        self.add_widget(Label(text=f"{lembretes[5]}",
                              font_size=20,
                              halign='left',
                              color=(0.5, 0.5, 0.5, 1),
                              text_size=(self.width * 12, None),
                              pos_hint={'x': 0.5,'center_y': 0.4},
                              ))

