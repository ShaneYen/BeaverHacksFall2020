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
import time
import sys

class Work_timer(Widget):
    a = NumericProperty(30)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.work_timer = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.work_timer.bind(on_complete=finish_callback)
        self.work_timer.start(self)

class MainWindow(Screen):
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)

    def countdown(self):
        # if self.set_number.text is '' or self.duration.text is '': #Error pops up if no numbers are inputted.
        #     self.show_popup()
        # else: #Jumps to TimerWindow and starts countdown otherwise. If we want to add a 3,2,1 countdown, probably put it here.
        # totalsets = int(self.set_number.text)
        # setduration = int(self.duration.text)
        sm.current = "timer"
        # TimerWindow().start_timer(totalsets, setduration)

    # def show_popup(self): #Error popup code
    #     content = Button(text='Please input numbers.')
    #     popupWindow = Popup(title="Error:", content=content, size_hint=(None, None), size=(300, 100), auto_dismiss=False)
    #     content.bind(on_press=popupWindow.dismiss)
    #     popupWindow.open()



class TimerWindow(Screen):
    counter = ObjectProperty(None)
    seconds = 50
    timer_message = StringProperty(str(seconds))

    def on_enter(self, *args):
        Clock.schedule_interval(self.update_time,1)


    def update_time(self, *args):
        self.seconds -= 1
        self.counter.text = str(self.seconds)




#
# class TimeApp(App):
#     def build(self):
#         crudeclock = Work_timer()
#         crudeclock.start()
#         return crudeclock



    # while seconds > 0:
    #     timer_message = StringProperty(str(seconds))
    #     time.sleep(1)
    #     seconds -= 1
    # def pause_button(self):
    #     print('pressed')

    # def start_timer(self, totalsets, setduration):
    #     #Placeholder Timer Logic
    #     setdurationoriginal=setduration
    #     while totalsets>0:
    #         if totalsets==1:
    #             print(totalsets, "set left.")
    #         else:
    #             print(totalsets, "sets left.")
    #         totalsets-=1
    #         while setduration>=0:
    #             if setduration==1:
    #                 print (setduration, "second left.")
    #             else:
    #                 print (setduration, "seconds left.")
    #             setduration-=1
    #         setduration=setdurationoriginal
    #     print ("FINISHED")


# class TimerWindow(Screen):
#     seconds = 50
#     timer_message = StringProperty(seconds)
#     while seconds > 0:
#         timer_message = StringProperty(seconds)
#         time.sleep(1)
#         seconds -= 1

    # def pause_button(self):
    #     print('pressed')

    # def start_timer(self, totalsets, work_duration, break_duration):
    #     #Placeholder Timer Logic
    #     setdurationoriginal=work_duration
    #     while totalsets>0:
    #         if totalsets==1:
    #             print(totalsets, "set left.")
    #         else:
    #             print(totalsets, "sets left.")
    #         totalsets-=1
    #         while work_duration>=0:
    #             if work_duration==1:
    #                 print (work_duration, "second left.")
    #             else:
    #                 print (work_duration, "seconds left.")
    #             work_duration-=1
    #         work_duration=setdurationoriginal
    #     print ("FINISHED")


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


