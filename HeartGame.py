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

# Reference format: "lead" = 13c4


def translateWordPartOne(text):
    for i in range(0, 26):
        if text[i] == 'a':
            letterValue = '01'
        elif text[i] == 'b':
            letterValue = '02'
        elif text[i] == 'c':
            letterValue = '03'
        elif text[i] == 'd':
            letterValue = '04'
        elif text[i] == 'e':
            letterValue = '05'
        elif text[i] == 'f':
            letterValue = '06'
        elif text[i] == 'g':
            letterValue = '07'
        elif text[i] == 'h':
            letterValue = '08'
        elif text[i] == 'i':
            letterValue = '09'
        elif text[i] == 'j':
            letterValue = '11'
        elif text[i] == 'k':
            letterValue = '12'
        elif text[i] == 'l':
            letterValue = '13'
        elif text[i] == 'm':
            letterValue = '14'
        elif text[i] == 'n':
            letterValue = '15'
        elif text[i] == 'o':
            letterValue = '16'
        elif letters[i] == 'p':
            letterValue = '17'
        elif letters[i] == 'q':
            letterValue = '18'
        elif text[i] == 'r':
            letterValue = '19'
        elif text[i] == 's':
            letterValue = '21'
        elif text[i] == 't':
            letterValue = '22'
        elif text[i] == 'u':
            letterValue = '23'
        elif text[i] == 'v':
            letterValue = '24'
        elif text[i] == 'w':
            letterValue = '25'
        elif text[i] == 'x':
            letterValue = '26'
        elif text[i] == 'y':
            letterValue = '27'
        elif text[i] == 'z':
            letterValue = '28'
        elif text[i] == '|':
            letterValue = '29'
        else:
            letterValue = '29'
    return letterValue


def translateWordPartTwo(letterEqualTo):
    if letterEqualTo == '01':
        basis = letterEqualTo[:2]
        print(basis)
        # print(letters[i])
        # letterValue = i + 2
        # print(letterValue)
        # i += 1

    # l / 12 / 1 + 2 = 3; z / 26 / 2 + 6 = 8   / method 1
    # if l, then c / if z, then h / method 2
    # for a in range(0, 26):


# trans = translateWordPartOne() + str(translateWordPartTwo(translateWordPartOne()))
# print(trans)


# if input = trans
# : "Correct Answer"

window.mainloop()
