import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button



class MainWindow(Screen):
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)

    def countdown(self):
        if self.set_number.text is '' or self.duration.text is '': #Error pops up if no numbers are inputted.
            self.show_popup()
        else: #Jumps to TimerWindow and starts countdown otherwise. If we want to add a 3,2,1 countdown, probably put it here.
            totalsets = int(self.set_number.text)
            setduration = int(self.duration.text)
            sm.current = "timer"
            TimerWindow().start_timer(totalsets, setduration)

    def show_popup(self): #Error popup code
        content = Button(text='Please input numbers.')
        popupWindow = Popup(title="Error:", content=content, size_hint=(None, None), size=(300, 100), auto_dismiss=False)
        content.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

class TimerWindow(Screen):
    timer_message = StringProperty('Timer Goes Here. Press to Pause/Continue')
    def pause_button(self):
        print('pressed')

    def start_timer(self, totalsets, setduration):
        #Placeholder Timer Logic
        setdurationoriginal=setduration
        while totalsets>0:
            if totalsets==1:
                print(totalsets, "set left.")
            else:
                print(totalsets, "sets left.")
            totalsets-=1
            while setduration>=0:
                if setduration==1:
                    print (setduration, "second left.")
                else:
                    print (setduration, "seconds left.")
                setduration-=1
            setduration=setdurationoriginal
        print ("FINISHED")


kv = Builder.load_file("main.kv")
sm = ScreenManager(transition=CardTransition())
sm.add_widget(MainWindow(name='main'))
sm.add_widget(TimerWindow(name='timer'))


class MainApp(App):
    def build(self):
        '''Main interface'''
        return sm

if __name__ == "__main__":
    MainApp().run() #.run method from App class


