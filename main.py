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
from kivy.core.window import Window
from functools import partial
import datetime
from kivy.core.audio import SoundLoader

work_bg_color = (182, 79, 200,1)
break_bg_color =(130,122, 137,1)

def kivy_color(tuple):
    return (tuple[0]/255, tuple[1]/255, tuple[2]/255, tuple[3])

class MainWindow(Screen):
    '''Starting screen where the user inputs the parameters of their workout.'''
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)
    break_duration = ObjectProperty(None)
    label_font_color = kivy_color(work_bg_color)

    def countdown(self):
        '''If parameters are properly set, saves the input values and moves to the TimerWindow screen.'''
        if self.set_number.text == '' or self.set_number.text == '0' or self.duration.text == '' or self.duration.text == '0' or self.break_duration.text == '' or self.break_duration.text == '0': #Error pops up if no numbers are inputted.
            self.show_popup()
        else: #Jumps to TimerWindow and starts countdown otherwise. If we want to add a 3,2,1 countdown, probably put it here.
            TimerWindow.sets = int(self.set_number.text)
            TimerWindow.work = int(self.duration.text)
            TimerWindow.break_dura = int(self.break_duration.text)
            sm.current = "timer"


    def show_popup(self):
        '''Error Popup for if the user does not input any numbers.'''
        content = Button(text='Please input numbers larger than 0.')
        popupWindow = Popup(title="Error:", content=content, size_hint=(None, None), size=(500, 100), auto_dismiss=False)
        content.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

class TimerWindow(Screen):
    '''Screen where the timer is displayed.'''
    counter = ObjectProperty(None)
    total_sets = ObjectProperty(None)
    work_duration = ObjectProperty(None)
    break_duration = ObjectProperty(None)
    current_timer = "work"

    def on_pre_enter(self, *args):
        self.work_duration = self.work
        self.total_sets = self.sets
        self.total_set_count = self.total_sets
        self.break_duration = self.break_dura
        self.workouttype.text = 'High Intensity'
        self.cyclesleft.text = ('0/' + str(self.total_set_count) + ' Sets Complete')

    def on_enter(self):
        '''Starts the count down when the screen is entered.'''
        sound = SoundLoader.load('timerstart.wav')
        sound.play()
        if self.total_sets > 0:
            self.clock = Clock.schedule_interval(self.update_time, 1) #Calls update_time method once a second.

    def on_leave(self):
        '''Resets all the parameters if stopping the timer.'''
        if self.pausebutton.text != 'Continue':
            self.clock.cancel()
        self.counter.text ='Go!'
        self.pausemessage.text =''
        self.pausebutton.text = 'Pause'
        self.current_timer = "work"
        self.cyclesleft.text = ('0/' + str(self.total_set_count) + ' Sets Complete')
        self.pausebutton.background_color = 0.125490196078431,0.141176470588235,0.129411764705882,1
        self.secondsaver = None

    def update_time(self, dt):
        '''Decrements the time left in the workout.'''
        self.cyclesleft.text = (str(self.total_set_count - self.total_sets) + '/' + str(self.total_set_count) + ' Sets Complete')
        if self.current_timer == "work":
            self.counter.text = str(self.work_duration)
            self.pausebutton.background_color = kivy_color(work_bg_color)
            self.workouttype.text= 'High Intensity'
            self.counter.text = str(datetime.timedelta(seconds=self.work_duration))[2:]
            self.work_duration -= 1
            if self.work_duration == 0 or self.work_duration == 1 or self.work_duration == 2:
                sound = SoundLoader.load('countdown.wav')
                sound.play()
            if self.work_duration < 0:
                self.total_sets -= 1
                if self.total_sets is not 0:
                    sound = SoundLoader.load('new_cycle.wav')
                    sound.play()
                self.current_timer = "break"
                self.break_duration = self.break_dura

        else:
            if self.total_sets>0:
                self.counter.text = str(datetime.timedelta(seconds=self.break_duration))[2:]
                self.pausebutton.background_color = kivy_color(break_bg_color)
                self.workouttype.text = 'Low Intensity'
                self.break_duration -= 1
                if self.break_duration == 0 or self.break_duration == 1 or self.break_duration == 2:
                    sound = SoundLoader.load('countdown.wav')
                    sound.play()
                if self.break_duration < 0:
                    sound = SoundLoader.load('new_cycle.wav')
                    sound.play()
                    self.current_timer = "work"
                    self.work_duration = self.work

        if self.total_sets < 1:
            self.cyclesleft.text = (str(self.total_set_count) + '/' + str(self.total_set_count) + ' Sets Complete')
            self.counter.text = 'FINISHED'
            sound = SoundLoader.load('timerfinished.wav')
            sound.play()
            self.clock.cancel()
            Clock.schedule_once(self.timer_finished, 2)

    def timer_finished(self, dt):
        sm.current = "main"

    def pause_button(self):
        '''Pause button functionality.'''
        if self.counter.text == 'FINISHED':
            pass
        elif self.pausebutton.text=='Continue':
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
        Window.clearcolor = (1,1,1,1)
        return sm

if __name__ == "__main__":
    MainApp().run() #.run method from App class