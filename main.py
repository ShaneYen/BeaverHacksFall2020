import kivy
from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.uix.floatlayout import FloatLayout
# from kivy.graphics import Rectangle
# from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class TimerWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        '''Main interface'''
        #return Label(text="test")
        #return FloatLayout()
        return kv

if __name__ == "__main__":
    MainApp().run() #.run method from App class


####Extra Code from learning Kivy basics, keeping it here for now in case I need to refer back to it
# class MyGrid(GridLayout):
#     '''Holds design elements'''
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols=1
#
#         #User parameters
#         self.timer_parameters=GridLayout()
#         self.timer_parameters.cols = 2
#
#         self.timer_parameters.add_widget(Label(text='# of Sets'))
#         self.number_of_sets = TextInput(multiline=False)
#         self.timer_parameters.add_widget(self.number_of_sets)
#
#         self.timer_parameters.add_widget(Label(text='Duration of each Set'))
#         self.set_duration = TextInput(multiline=False)
#         self.timer_parameters.add_widget(self.set_duration)
#
#         self.add_widget(self.timer_parameters)
#
#         #Start button
#         self.submit = Button(text="Start", font_size=40)
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget (self.submit)
#
#     def pressed(self, instance):
#         totalsets= self.number_of_sets.text
#         setduration=self.set_duration.text
#         print(totalsets + setduration)

# class MyGrid(Widget):
#     set_number = ObjectProperty(None)
#     duration = ObjectProperty(None)
#     # pythoncode:ID <- for global variables in kv file
#
#     def button_press(self):
#         print("Number of sets:", self.set_number.text)
#         print("Duration of sets:", self.duration.text)
#         self.set_number.text=""
#         self.duration.text=""

#kv file has to be the name of the main class (- app) Ex: MyApp= my.kv

# class Touch(Widget):
#     btn = ObjectProperty(None)
#
#     def on_touch_down(self, touch):
#         print("Mouse Down", touch)
#         self.btn.opacity=0.5
#     def on_touch_move(self, touch):
#         print("Mouse Move", touch)
#     def on_touch_up(self, touch):
#         print("Mouse Up", touch)
#         self.btn.opacity = 1

