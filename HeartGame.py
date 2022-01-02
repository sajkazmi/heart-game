# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

import random
import tkinter
from tkinter import*
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=10, bg='blue')
letterValue = ""

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

randomWord = generateWord()

Label(window, text=randomWord).grid(row=0, column=1)


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
# Reference format: "medicare" = 14d8

# Part One: Initial Letter
# Part Two: basis
# Part Three: length of word


def translateWordPartOne(randomWord):
    # for i in range(0, 26):
    if randomWord[0] == 'a':
        letterValue = '01'
    elif randomWord[0] == 'b':
        letterValue = '02'
    elif randomWord[0] == 'c':
        letterValue = '03'
    elif randomWord[0] == 'd':
        letterValue = '04'
    elif randomWord[0] == 'e':
        letterValue = '05'
    elif randomWord[0] == 'f':
        letterValue = '06'
    elif randomWord[0] == 'g':
        letterValue = '07'
    elif randomWord[0] == 'h':
        letterValue = '08'
    elif randomWord[0] == 'i':
        letterValue = '09'
    elif randomWord[0] == 'j':
        letterValue = '11'
    elif randomWord[0] == 'k':
        letterValue = '12'
    elif randomWord[0] == 'l':
        letterValue = '13'
    elif randomWord[0] == 'm':
        letterValue = '14'
    elif randomWord[0] == 'n':
        letterValue = '15'
    elif randomWord[0] == 'o':
        letterValue = '16'
    elif randomWord[0] == 'p':
        letterValue = '17'
    elif randomWord[0] == 'q':
        letterValue = '18'
    elif randomWord[0] == 'r':
        letterValue = '19'
    elif randomWord[0] == 's':
        letterValue = '21'
    elif randomWord[0] == 't':
        letterValue = '22'
    elif randomWord[0] == 'u':
        letterValue = '23'
    elif randomWord[0] == 'v':
        letterValue = '24'
    elif randomWord[0] == 'w':
        letterValue = '25'
    elif randomWord[0] == 'x':
        letterValue = '26'
    elif randomWord[0] == 'y':
        letterValue = '27'
    elif randomWord[0] == 'z':
        letterValue = '28'
    else:
        letterValue = '29'
    return letterValue


# Part Two: basis
# Reference format: "medicare" = 14d8
# Reference format: "moments" = 14d7
def translateWordPartTwo(letterValue):
    if letterValue[-1] == '1':
        basis = 'a'
    elif letterValue[-1] == '2':
        basis = 'b'
    elif letterValue[-1] == '3':
        basis = 'c'
    elif letterValue[-1] == '4':
        basis = 'd'
    elif letterValue[-1] == '5':
        basis = 'e'
    elif letterValue[-1] == '6':
        basis = 'f'
    elif letterValue[-1] == '7':
        basis = 'g'
    elif letterValue[-1] == '8':
        basis = 'h'
    else:
        basis = 'i'
    print(basis)
    return basis


translateWordPartOne(randomWord)
translateWordPartTwo(letterValue)

# print(translateWordPartOne(randomWord))
# print(translateWordPartTwo(randomWord))


window.mainloop()
