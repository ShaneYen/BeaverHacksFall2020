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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class MainWindow(Screen):
    set_number = ObjectProperty(None)
    duration = ObjectProperty(None)


    def countdown(self):
        totalsets= int(self.set_number.text)
        setduration=int(self.duration.text)
        TimerWindow().start_timer(totalsets, setduration)

class TimerWindow(Screen):
    def pause(self):
        print('pressed')

    def start_timer(self, totalsets, setduration):
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


