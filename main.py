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
from functools import partial
import datetime

#str(datetime.timedelta(seconds=666))
#= 0:11:06

class MainWindow(Screen):
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)

    def countdown(self):
        if self.set_number.text is '' or self.duration.text is '': #Error pops up if no numbers are inputted.
            self.show_popup()
        else: #Jumps to TimerWindow and starts countdown otherwise. If we want to add a 3,2,1 countdown, probably put it here.
            TimerWindow.totalsets = int(self.set_number.text)
            TimerWindow.setduration = int(self.duration.text)
            sm.current = "timer"


    def show_popup(self): #Error popup code
        content = Button(text='Please input numbers.')
        popupWindow = Popup(title="Error:", content=content, size_hint=(None, None), size=(300, 100), auto_dismiss=False)
        content.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

class TimerWindow(Screen):
    counter = ObjectProperty(None)
    seconds= NumericProperty(0)

    def on_enter(self):
        self.seconds = self.setduration
        self.clock=Clock.schedule_interval(self.update_time, 1)

    # def update_time(self, dt):
    #     self.counter.text = str(self.seconds)
    #     if self.counter.seconds < 0:
    #         self.counter.text = 'FINISHED'
    #         self._clock.cancel()
    #         del self._clock
    #     else:
    #         self.seconds -= 1

    def update_time(self, dt):
        self.counter.text = str(self.seconds)
        self.seconds -= 1
        if self.seconds < 0:
            self.counter.text = 'FINISHED'
            self.clock.cancel()

    def pause_button(self):
        print('press')

class WindowManager(ScreenManager):
    pass

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


