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
    '''Starting screen where the user inputs the parameters of their workout.'''
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)
    break_duration = ObjectProperty(None)

    def countdown(self):
        '''If parameters are properly set, saves the input values and moves to the TimerWindow screen.'''
        if self.set_number.text is '' or self.duration.text is '': #Error pops up if no numbers are inputted.
            self.show_popup()
        else: #Jumps to TimerWindow and starts countdown otherwise. If we want to add a 3,2,1 countdown, probably put it here.
            TimerWindow.sets = int(self.set_number.text)
            TimerWindow.work = int(self.duration.text)
            TimerWindow.break_dura = int(self.break_duration.text)
            sm.current = "timer"


    def show_popup(self):
        '''Error Popup for if the user does not input any numbers.'''
        content = Button(text='Please input numbers.')
        popupWindow = Popup(title="Error:", content=content, size_hint=(None, None), size=(300, 100), auto_dismiss=False)
        content.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

class TimerWindow(Screen):
    '''Screen where the timer is displayed.'''
    counter = ObjectProperty(None)
    total_sets = ObjectProperty(None)
    work_duration = ObjectProperty(None)
    break_duration = ObjectProperty(None)

    current_timer = "work"
    init_work = ObjectProperty(None)
    init_break = ObjectProperty(None)


    def on_enter(self):
        '''Starts the count down when the screen is entered.'''
        self.work_duration = self.work
        self.total_sets = self.sets
        self.break_duration = self.break_dura

        if self.total_sets > 0:
            self.clock = Clock.schedule_interval(self.update_time, 1) #Calls update_time method once a second.

    def on_leave(self):
        '''Resets all the parameters if stopping the timer.'''
        if self.pausebutton.text != 'Continue':
            self.clock.cancel()
            # del self.clock
        self.counter.text ='Go!'
        self.pausemessage.text =''
        self.pausebutton.text = 'Pause'
        self.secondsaver = None

    def update_time(self, dt):
        '''Decrements the time left in the workout.'''
        if self.current_timer == "work":
            self.counter.text = str(self.work_duration)
            self.work_duration -= 1
        else:
            self.counter.text = str(self.break_duration)
            self.break_duration -= 1

        if self.counter.text == "0":
            if self.current_timer == "work":
                self.total_sets -= 1
                self.current_timer = "break"
                self.break_duration = self.break_dura
            else:
                self.current_timer = "work"
                self.work_duration = self.work

        if self.total_sets < 0:
            self.counter.text = 'FINISHED'
            self.clock.cancel()

    def pause_button(self):
        '''Pause button functionality.'''
        if self.pausebutton.text=='Continue':
            self.pausebutton.text = 'Pause'
            self.pausemessage.text = ''
            self.work_duration=self.second_saver
            self.clock = Clock.schedule_interval(self.update_time, 1)
        else:
            self.pausebutton.text = 'Continue'
            self.pausemessage.text = 'TIMER PAUSED'
            self.second_saver = self.work_duration
            self.clock.cancel()
            del self.clock






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


