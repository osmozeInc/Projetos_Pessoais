from kivy.app import App
from kivy.lang import Builder
from Back_end.data_base import *
from Back_end.kivy_elements import *
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from Back_end.validation import Validation
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


Builder.load_file('Front-end/class.kv')
Builder.load_file('Front-end/task.kv')
Builder.load_file('Front-end/reminder.kv')
Builder.load_file('Front-end/project.kv')

sm = ScreenManager(transition = NoTransition())


class MyApp(App):
    def build(self):
        Window.maximize()

        sm.add_widget(Task(name='task'))
        sm.add_widget(Reminder(name='reminder'))
        sm.add_widget(Project(name='project'))
        sm.add_widget(New_Task(name='new_task'))
        sm.add_widget(New_Reminder(name='new_reminder'))
        sm.add_widget(New_Project(name='new_project'))

        nav_bar = NavigationBar(orientation='horizontal')

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(nav_bar)
        layout.add_widget(sm)
        return layout


class NavigationBar(Screen, BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Press_Reminder()
    
    def Press_Task(self):
        if self.ids.task_line.opacity == 0:
            self.ids.task_line.opacity = 1

        if self.ids.reminder_line.opacity == 1:
            self.ids.reminder_line.opacity = 0

        if self.ids.project_line.opacity == 1:
            self.ids.project_line.opacity = 0

        sm.current = 'task'

    def Press_Reminder(self):
        if self.ids.reminder_line.opacity == 0:
            self.ids.reminder_line.opacity = 1

        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.project_line.opacity == 1:
            self.ids.project_line.opacity = 0

        sm.current = 'reminder'

    def Press_Project(self):
        
        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.reminder_line.opacity == 1:
            self.ids.reminder_line.opacity = 0

        if self.ids.project_line.opacity == 0:
            self.ids.project_line.opacity = 1
            
        sm.current = 'project'

class Task(Screen):
    def Create_New_Task(self):
        sm.current = 'new_task'

class New_Task(Screen):
    pass

class Reminder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Validate = Validation()
        self.Read_DB = Read_DB()

    def on_enter(self):
        lembretes = self.Read_Reminder()
        box_layout = self.ids.box_layout

        for i in range(len(lembretes)):
            element = Element_FloatLayout_Class(lembretes[i])
            box_layout.add_widget(element)

    def Create_New_Reminder(self):
        sm.current = 'new_reminder'

    def Read_Reminder(self):
        lembretes = self.Read_DB.Read_Reminder()
        return lembretes
        
class New_Reminder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Validate = Validation()
        self.Update_DB = Update_DB()

    def Cancel_New_Reminder(self):
        sm.current = 'reminder'
    
    def Save_New_Reminder(self, name, date, time, description, link):
        check_1, check_2 = 0, 0
        self.Validate_Title(name)
        check_1 = self.Validate_Date(date)
        check_2 = self.Validate_Time(time)
        self.Validate_Description(description)
        self.Validate_Link(link)

        if check_1 == 0 and check_2 == 0:

            name = name.text
            date = date.text
            time = time.text
            description = description.text
            link = link.text

            self.Update_DB.Update_Lembrete(name, date, time, description, link)
            sm.current = 'reminder'

        else:
            pass

    def Validate_Title(self, instance):
        Validation.Validate_Title(self, instance)
        
    def Validate_Date(self, instance):
        if Validation.Validate_Date(self, instance) == 0:
            return 0
        else:
            return 1

    def Validate_Time(self, instance):
        if Validation.Validate_Time(self, instance) == 0:
            return 0
        else:
            return 1
        
    def Validate_Description(self, instance):
        Validation.Validate_Description(self, instance)

    def Validate_Link(self, instance):
        Validation.Validate_Link(self, instance)

class Project(Screen):
    def Create_New_Project(self):
        sm.current = 'new_project'

class New_Project(Screen):
    pass

if __name__ == '__main__':
    Create_DB()
    MyApp().run()