# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

import tkinter
from tkinter import*
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=100, bg='blue')

buttons = ['i', 'r', '|', '9',
           'h', 'q', 'z', '8',
           'g', 'p', 'y', '7',
           'f', 'o', 'x', '6',
           'e', 'n', 'w', '5',
           'd', 'm', 'v', '4',
           'c', 'l', 'u', '3',
           'b', 'k', 't', '2',
           'a', 'j', 's', '1',
           '0', '1', '2', '/']

inpu.grid(row=0, column=0)


def dispButtons():
    for button in buttons:
        tkinter.Button(window, text=button, width=3, bd=12, font=('arial', 12, ' bold'), bg='blue',
                       activebackground="#ffffff", activeforeground="#000990", relief="raised", command=convertInput).grid(
            row=5, column=1)


dispButtons()


window.mainloop()
