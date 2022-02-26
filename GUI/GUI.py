import PySimpleGUI as sg
from time import sleep
import os
import sys
script_dir = os.path.dirname( __file__ )
func_dir = os.path.join(script_dir, "..", "Functions")
sys.path.append(func_dir)
import Functions.main_functions as func

class screen:
    def __init__(self):
        """
        GUI Starting configs
        
        """



        sg.theme(new_theme="DarkPurple1")

        layout = [
            [sg.Text('Keyword:'),sg.Input(size=(20,0),key="keyword")],
            [sg.Text('How many pages should the bot do? '),sg.Slider(range=(1, 10),default_value=1,orientation='h',key="people_loop")],
            [sg.Button('Start')],
            [sg.Output(size=(65,20))]
        ]
        self.window = sg.Window("LinkedIn Auto-connect", layout, size=(400,300), element_justification="center")

    def run(self):
        """
        Start the program's interface

        """
        while True:
            self.events, self.values = self.window.Read()
            if self.events == sg.WIN_CLOSED:
                break
            else:
                bot = func.Linkedin_autoConnect()
                bot.run(self.values['keyword'], self.values['people_loop'])
                break
        self.window.Close()

    def popup(self):
        sg.Popup("Click me whe you are logged in :)", keep_on_top=True)
