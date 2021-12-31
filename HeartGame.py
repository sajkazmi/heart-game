# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

import random
import tkinter
from tkinter import*
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=10, bg='blue')


with open("./wordlist.10000.txt") as word_file:
    words = word_file.read().split()


def generateWord():
    translate = random.choice(words)
    return translate


buttons = [['i', 'r', '|', '9'],
           ['h', 'q', 'z', '8'],
           ['g', 'p', 'y', '7'],
           ['f', 'o', 'x', '6'],
           ['e', 'n', 'w', '5'],
           ['d', 'm', 'v', '4'],
           ['c', 'l', 'u', '3'],
           ['b', 'k', 't', '2'],
           ['a', 'j', 's', '1'],
           ['0', '1', '2', '/']]

inpu.grid(row=0, column=0)

Label(window, text=generateWord()).grid(row=0, column=1)


def dispButtons():
    r = 1
    for row in buttons:
        c = 1
        for column in row:
            Button(window, text=column).grid(row=r, column=c)
            c += 1
        r += 1


dispButtons()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Reference format: "lead" = 12c4


def translateWord():
    for i in range(0, 26):
        print(letters[i])
        letterValue = i + 1
        print(letterValue)
        i += 1

    # l / 12 / 1 + 2 = 3; z / 26 / 2 + 6 = 8   / method 1
    if l, then c / if z, then h / method 2
    # for a in range(0, 26):


translateWord()

window.mainloop()
