# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

from tkinter import*
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=100, bg='blue')

button = ['a', 'b', 'c', 'd']

inpu.grid(row=0, column=0)
window.mainloop()
