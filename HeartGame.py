# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# To solve the cycling problem, you need to look at the incorrect statement as ans should not be same for both correct and incorrect, USE DIFFERENT ARRAY VALUES.

# To fix GUI alignment, just de indent.
# string index error is being caused by you accessing word characterd instead of different words, through arrayfication. May need numPy.

# python\python310\site-packages is Windows location for Python and numpy. I have to add the path to this on Termux to install numpy.

# There is no need for ToTranslateAFTER or ansAFTER, just use the arrayfication of ToTranslate.

# solution value suggests ans is not correct.

# end-1c can be used to get the last character of the string, / may be mismatching with the correct answer.

import tkinter as tk
from functools import partial
from tkinter import messagebox
from tkinter import*
import tkinter
import random
import numpy as np


with open("./wordlist.10000.txt") as word_file:
    words = word_file.read().split()


Keyboard_App = tkinter.Tk()
Keyboard_App.title("Heart Game")
Keyboard_App['bg'] = 'blue'
Keyboard_App.geometry("415x705")


def generateWord(c):
    translate = random.choice(words)
    return translate


def iterToTrans(counter):
    ToTranslate = np.str_(generateWord(counter))
    return ToTranslate


def displayTablet(SourceText):
    # Following was source of word disappearing bug:
    label1 = Label(Keyboard_App, text="Visual Memory TABLET"+"\n"+str(SourceText), font=(
        "arial", 20, 'bold'), fg='yellow', bg='blue').grid(row=0, columnspan=40, padx=30, sticky=W)


def redeploy(ToTrans):
    answer = interpreter(ToTrans)
    return answer


def select(value, k):
    if value == "/":
        ans = np.array([], dtype=object)
        ToTranslat = iterToTrans(k)
        ans = np.append(ans, redeploy(ToTranslat))
        displayTablet(ToTranslat)
        print("ans: ", ans[k])
        inpu = sentry.get("1.0", 'end-2c')
        print("input: ", inpu)
        if inpu == ans[k-1]:
            messagebox.showinfo("Result", "CORRECT!")

        else:
            messagebox.showinfo(
                "Result", "Incorrect; the Correct answer is:\n                   " + ans[k])


def interpreter(SourceWord):
    correctNotationInitial = SourceWord[0]

    # Alphabet Numerical Equivalence follows:
    if correctNotationInitial == '0':
        Box = "00"
    elif correctNotationInitial == 'a':
        Box = "01"
    elif correctNotationInitial == 'b':
        Box = "02"
    elif correctNotationInitial == 'c':
        Box = "03"
    elif correctNotationInitial == 'd':
        Box = "04"
    elif correctNotationInitial == 'e':
        Box = "05"
    elif correctNotationInitial == 'f':
        Box = "06"
    elif correctNotationInitial == 'g':
        Box = "07"
    elif correctNotationInitial == 'h':
        Box = "08"
    elif correctNotationInitial == 'i':
        Box = "09"
    elif correctNotationInitial == '1':
        Box = "10"
    elif correctNotationInitial == 'j':
        Box = "11"
    elif correctNotationInitial == 'k':
        Box = "12"
    elif correctNotationInitial == 'l':
        Box = "13"
    elif correctNotationInitial == 'm':
        Box = "14"
    elif correctNotationInitial == 'n':
        Box = "15"
    elif correctNotationInitial == 'o':
        Box = "16"
    elif correctNotationInitial == 'p':
        Box = "17"
    elif correctNotationInitial == 'q':
        Box = "18"
    elif correctNotationInitial == 'r':
        Box = "19"
    elif correctNotationInitial == '2':
        Box = "20"
    elif correctNotationInitial == 's':
        Box = "21"
    elif correctNotationInitial == 't':
        Box = "22"
    elif correctNotationInitial == 'u':
        Box = "23"
    elif correctNotationInitial == 'v':
        Box = "24"
    elif correctNotationInitial == 'w':
        Box = "25"
    elif correctNotationInitial == 'x':
        Box = "26"
    elif correctNotationInitial == 'y':
        Box = "27"
    elif correctNotationInitial == 'z':
        Box = "28"
    else:
        Box = "29"

    BoxFirst = Box[0]
    BoxSecond = Box[1]
    length = str(len(SourceWord))
    # print(length)

    # Root letters
    if BoxSecond == "1":
        ANE = "a"
    elif BoxSecond == "2":
        ANE = "b"
    elif BoxSecond == "3":
        ANE = "c"
    elif BoxSecond == "4":
        ANE = "d"
    elif BoxSecond == "5":
        ANE = "e"
    elif BoxSecond == "6":
        ANE = "f"
    elif BoxSecond == "7":
        ANE = "g"
    elif BoxSecond == "8":
        ANE = "h"
    elif BoxSecond == "9":
        ANE = "i"

    correctNOTATION = BoxFirst+BoxSecond+ANE+length
    return correctNOTATION


def detectClicks(button):
    # for adjusting location and size of text box

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

    for button in buttons:
        def command(button):
            select(button, 0)
        varRow = 2
        varColumn = 0

        tkinter.Button(Keyboard_App, text=button, width=3, bd=12, font=('arial', 12, ' bold'), bg='blue',
                       activebackground="#ffffff", activeforeground="#000990", relief="raised", command=command).grid(
            row=varRow, column=varColumn)

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

    return buttons


entry = Text(Keyboard_App, width=138, height=2, font=('arial', 10, 'bold'))
entry.grid(row=1, columnspan=40, pady=10)
sentry = entry.insert(tkinter.END, "")  # insert value into text box

Keyboard_App.mainloop()
