from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from Back_end.validation import Validation
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from Back_end.data_base import *
from Back_end.kivy_elements import *





class MyApp(MDApp):
    def build(self):
        Window.maximize()
        self.sm = ScreenManager(transition = NoTransition())

        self.sm.add_widget(Task(name='task'))
        self.sm.add_widget(Reminder(name='reminder'))
        self.sm.add_widget(Project(name='project'))
        self.sm.add_widget(New_Task(name='new_task'))
        self.sm.add_widget(New_Reminder(name='new_reminder'))
        self.sm.add_widget(New_Project(name='new_project'))

        nav_bar = NavigationBar(orientation='horizontal')

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(nav_bar)
        layout.add_widget(self.sm)
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
        app = App.get_running_app()
        app.sm.current = 'task'

    def Press_Reminder(self):
        if self.ids.reminder_line.opacity == 0:
            self.ids.reminder_line.opacity = 1

        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.project_line.opacity == 1:
            self.ids.project_line.opacity = 0

        app = App.get_running_app()
        app.sm.current = 'reminder'

    def Press_Project(self):
        
        if self.ids.task_line.opacity == 1:
            self.ids.task_line.opacity = 0

        if self.ids.reminder_line.opacity == 1:
            self.ids.reminder_line.opacity = 0

        if self.ids.project_line.opacity == 0:
            self.ids.project_line.opacity = 1
            
        app = App.get_running_app()
        app.sm.current = 'project'

    def Update_Screen(self, screen):
        app = App.get_running_app()
        app.sm.current = screen

class Task(Screen):
    def Create_New_Task(self):
        app = App.get_running_app()
        app.sm.current = 'new_task'

class New_Task(Screen):
    pass

class Reminder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Validate = Validation()
        self.Read_DB = Read_DB()

    def on_enter(self):
        lembretes = self.Read_DB.Read_Reminder()
        box_layout = self.ids.box_layout
        box_layout.clear_widgets()

        for i in range(len(lembretes)):
            element = Element_Reminder_FloatLayout_Class(lembretes[i])
            box_layout.add_widget(element)

    def Create_New_Reminder(self):
        app = App.get_running_app()
        app.sm.current = 'new_reminder'

class New_Reminder(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Validate = Validation()
        self.Update_DB = Update_DB()

    def Cancel_New_Reminder(self):
        app = App.get_running_app()
        app.sm.current = 'reminder'
    
    def Save_New_Reminder(self, name, date, time, description, link):
        check_1, check_2 = 0, 0
        self.Validate_Title(name)
        check_1 = self.Validate_Date(date)
        check_2 = self.Validate_Time(time)
        self.Validate_Description(description)
        self.Validate_Link(link)

        if check_1 == 0 and check_2 == 0:
            self.Update_DB.Update_Lembrete(name.text, date.text, date.text, description.text, link.text)

            self.ids.title_new_reminder.text = ''
            self.ids.date_new_reminder.text = ''
            self.ids.time_new_reminder.text = ''
            self.ids.description_new_reminder.text = ''
            self.ids.link_new_reminder.text = ''

            app = App.get_running_app()
            app.sm.current = 'reminder'

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
        app = App.get_running_app()
        app.sm.current = 'new_project'

class New_Project(Screen):
    pass


if __name__ == '__main__':
    Create_DB()
    Builder.load_file('Front-end/class.kv')
    Builder.load_file('Front-end/task.kv')
    Builder.load_file('Front-end/reminder.kv')
    Builder.load_file('Front-end/project.kv')
    MyApp().run()