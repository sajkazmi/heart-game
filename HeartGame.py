# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled
# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

import random
import tkinter
from tkinter import*
from functools import partial
import tkinter as tk

# app = tk.Tk()
# app.geometry("40x40")

with open("./wordlist.10000.txt") as word_file:
    words = word_file.read().split()


Keyboard_App = tkinter.Tk()
Keyboard_App.title("Heart Game")
Keyboard_App['bg'] = 'blue'
#Keyboard_App.resizable(0, 0)
Keyboard_App.geometry("350x625")


def select(value):
    if value == " Space ":
        entry.insert(tkinter.END, '   ')

    elif value == "Tab":
        entry.insert(tkinter.END, '     ')
    else:
        entry.insert(tkinter.END, value)


label1 = Label(Keyboard_App, text="Visual Memory TABLET"+"\n"+(random.choice(words)), font=(
    "arial", 20, 'bold'), fg='yellow', bg='blue').grid(row=0, columnspan=40, sticky=W)

# for adjusting location and size of text box
entry = Text(Keyboard_App, width=138, height=2, font=('arial', 10, 'bold'))
entry.grid(row=1, columnspan=40, pady=10)

buttons = ['I', 'R', 'Pipe', '9',
           'H', 'Q', 'Z', '8',
           'G', 'P', 'Y', '7',
           'F', 'O', 'X', '6',
           'E', 'N', 'W', '5',
           'D', 'M', 'V', '4',
           'C', 'L', 'U', '3',
           'B', 'K', 'T', '2',
           'A', 'J', 'S', '1',
           '0', '1', '2', 'Level']

varRow = 2
varColumn = 0

for button in buttons:
    def command(x=button): select(x)
    if button != " Level ":
        tkinter.Button(Keyboard_App, text=button, width=5, bd=12, font=('arial', 10, ' bold'), bg='blue',
                       activebackground="#ffffff", activeforeground="#000990", relief="raised", command=command).grid(
            row=varRow, column=varColumn)

    if button == " Level ":
        tkinter.Button(Keyboard_App, text=button, width=118, bd=12, font=('arial', 10, ' bold'), bg='blue',
                       activebackground="#ffffff", activeforeground="#000990", relief="raised", command=command).grid(
            row=6, column=4)

    varColumn += 1
    if varColumn > 3 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 6:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 7:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 8:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 9:
        varColumn = 0
        varRow += 1
    if varColumn > 3 and varRow == 10:
        varColumn = 0
        varRow += 1
Keyboard_App.mainloop()
