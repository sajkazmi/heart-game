# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

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
window.mainloop()
