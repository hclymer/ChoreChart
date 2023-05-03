import PySimpleGUI as sg 
from chorechart_fun import chorechart
import pandas as pd

sg.theme("DarkAmber")

layout = [[sg.Text("Chore Chart")],
          [sg.InputText(key="dchore 1")],
          [sg.InputText(key="dchore 2")],
          [sg.InputText(key="dchore 3")],
          [sg.InputText(key="dchore 4")],
          [sg.InputText(key="dchore 5")],
          [sg.InputText(key='wchore 1')],
          [sg.InputText(key='wchore 2')],
          [sg.Submit(), sg.Cancel()]
          ]


window = sg.Window("Chore Chart", layout)

event, values = window.read()

window.close()


list1 = []
list2 = []

list1.append(values['dchore 1'])
list1.append(values['dchore 2'])
list1.append(values['dchore 3'])
list1.append(values['dchore 4'])
list1.append(values['dchore 5'])
list2.append(values['wchore 1'])
list2.append(values['wchore 2'])


sg.popup("Your chore list is:" ,chorechart(daily_chores= list1, weekly_chores=list2))
         