from tkinter import *

import pyperclip

screen = Tk()

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}


# ----convert to morse code----


def text_to_morse():
    morse_out.delete('1.0', END)

    input = text_input.get().upper()

    output = []

    for n in input:
        output.append(MORSE_CODE_DICT[n])

    morsecode = "".join(output)
    print(morsecode)

    morse_out.insert(END, morsecode)
    pyperclip.copy(morsecode)



# ----UI----

screen.title("Text to Morse Code")
screen.minsize(width=200, height=100)
screen.config(padx=50, pady=50)

input_label = Label(text="Input")
input_label.grid(row=0, column=0)

text_input = Entry(width=46)
text_input.grid(row=0, column=1)
text_input.focus()

output_label = Label(text="Output")
output_label.grid(row=1, column=0)

morse_out = Text(width=60, height=10)
morse_out.grid(row=1, column=1)

button = Button(text="Convert to morsecode", command=text_to_morse)
button.grid(row=2, column=1)

screen.mainloop()
