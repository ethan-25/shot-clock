# This script will display a dialogue box that asks the user for a player name.
# When a valid player name is typed, the user has the option to see player stats or their shot chart, where playerfind.py or shotchart.py will run based on user option.

import player_info
import variable
import tkinter as tk

t = tk.Tk()

display = tk.Canvas(t, width=250, height=150, bg="black",
                    relief='raised')
display.pack()

label = tk.Label(t, text="NBA Shotchart Visualizer", bg="black", fg="white")
label.config(font=("bold", 14))
display.create_window(120, 25, window=label)

icon = tk.Label(t, text="🏀", bg="black", fg="white")
icon.config(font=("bold", 14))
display.create_window(120, 50, window=icon)

label2 = tk.Label(t, text='Find your player:', bg="black", fg="white")
label2.config(font=("bold", 10))
display.create_window(120, 75, window=label2)

entry = tk.Entry(t)
display.create_window(120, 100, window=entry)


def getChart():
    variable.playerName = entry.get()
    player_info.find_player(variable.playerName)
    t.destroy()


def helpWindow():
    t2 = tk.Tk()

    label = tk.Label(t2, text="Shotchart won't generate?",
                     bg="black", fg="white")
    label.config(font=("bold", 14))
    label.pack()

    label2 = tk.Label(t2, text="This might be due to your input\nbeing formatted wrong.\n\nMake sure you have the player's:\n-First and last name\n-First letters being uppercase\nEx. Lebron James\n\nThis program does not accept\nanything but a string",
                      bg="black", fg="white")
    label2.config(font=(9))
    label2.pack()


generate_btn = tk.Button(text='Generate Shotchart', command=getChart,
                         bg='white', fg='black')
display.create_window(120, 135, window=generate_btn)

help_btn = tk.Button(text='?', command=helpWindow,
                     bg='white', fg='black')
display.create_window(225, 135, window=help_btn)

t.mainloop()
