class Validation:
    def __init__(self):
        pass

    def Validate_Title(self, instance):
        if len(instance.text) > 40:
            instance.text = instance.text[:40].title()
        else:
            instance.text = instance.text.title()
        
    def Validate_Date(self, instance):
        text = instance.text

        if text == '':
            self.ids.date_new_reminder.hint_text = 'Digite a data (somente numeros)'
            return 1
        
        if text[2] == '/' and text[5] == '/':
            pass

        else:
            if len(text) > 8:
                instance.text = text[:8]
                text = text[:8]

            if len(text) < 8:
                instance.text = ''
                self.ids.date_new_reminder.hint_text = 'Data invalida, repita'
                return 1

            if len(text) == 8:
                instance.text = text[:2] + '/' + text[2:4] + '/' + text[4:]
            
        return 0

    def Validate_Time(self, instance):
        text = instance.text
        if text == '':
            self.ids.time_new_reminder.hint_text = 'Digite a hora (somente numeros)'
            return 1
        
        if text[2] == ':' and len(text) == 5:
            pass

        else:
            if len(text) > 4:
                instance.text = text[:4]
                text = text[:4]

            if len(text) < 4:
                    instance.text = ''
                    self.ids.time_new_reminder.hint_text = 'Hora invalida, repita'
                    return 1
            
            if len(text) == 4:
                hora = text[:2]
                minuto = text[2:]

                if int(hora) > 23 or int(minuto) > 59:
                    instance.text = ''
                    self.ids.time_new_reminder.hint_text = 'Hora invalida, repita'
                    return 1

                instance.text = text[:2] + ':' + text[2:]

            
        return 0

    def Validate_Description(self, instance):
        if len(instance.text) > 200:
            instance.text = instance.text[:200]

    def Validate_Link(self, instance):
        if instance.text == '':
            instance.text = 'https://'
