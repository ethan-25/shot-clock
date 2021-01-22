# This script will display a dialogue box that asks the user for a player name.
# When a valid player name, season year, and season type is inputted, the user can see their player data in the form of a shot chart or a table (maybe, I don't know.)

import player_info
import variable
import tkinter as tk
from tkinter import messagebox

# Button functions.


def getChart():
    # If all entry boxes and toggle buttons are valid, then functions in player_info.py will run

    # This checks if the user forgets to toggle a season type button. A message box will pop up if they do.
    if variable.seasonType == "":
        messagebox.showinfo(
            title="Error: No Season Type Found", message="You must toggle a season type.",)

    # Else, assign the variables in variable.py to user inputs
    else:
        variable.playerName = playerEntry.get()
        variable.seasonYear = seasonyearEntry.get()
        # This part will test the acquired values for playerName and seasonYear
        try:
            player_info.find_player(variable.playerName)
            # I'll add something here later that makes sure seasonYear has a valid entry.
            t.destroy()
        # If an error occurs a message box will pop up with a message asking the user to fix their entry
        except:
            messagebox.showinfo(
                title="Input Error", message="Enter a valid player full name or season year\n\nExample: LeBron James")


def toggleButton():
    # Toggles between seasonType whenever the user presses the respective button
    if regButton["relief"] == "raised":
        regButton.configure(relief="sunken")
        poButton.configure(relief="raised")
        variable.seasonType = "Regular Season"

    elif poButton["relief"] == "raised":
        regButton.configure(relief="raised")
        poButton.configure(relief="sunken")
        variable.seasonType = "Playoffs"


# GUI/Tkinter stuff, pretty much a mess.
t = tk.Tk()
display = tk.Canvas(t, width=250, height=250, bg="black",
                    relief="raised")
display.pack()

# Title
title_label = tk.Label(
    t, text="NBA Shotchart Visualizer", bg="black", fg="white")
title_label.config(font=("bold", 14))
display.create_window(125, 25, window=title_label)

# Little basketball icon
icon = tk.Label(t, text="🏀", bg="black", fg="white")
icon.config(font=("bold", 14))
display.create_window(125, 50, window=icon)

# Player name entry
player_label = tk.Label(t, text="Enter a player name:", bg="black", fg="white")
player_label.config(font=("bold", 10))
display.create_window(125, 75, window=player_label)
playerEntry = tk.Entry(t)
display.create_window(125, 100, window=playerEntry)

# Season entry
season_label = tk.Label(t, text="Enter season year (Ex. 2020-21):",
                        bg="black", fg="white")
season_label.config(font=("bold", 10))
display.create_window(125, 125, window=season_label)
seasonyearEntry = tk.Entry(t)
display.create_window(125, 150, window=seasonyearEntry)

# Season type toggle buttons
regButton = tk.Button(text="Regular Season", width=12,
                      relief="raised", command=toggleButton)
poButton = tk.Button(text="Playoffs", width=12,
                     relief="raised", command=toggleButton)
display.create_window(80, 185, window=regButton)
display.create_window(170, 185, window=poButton)

# Execute the main function
generate = tk.Button(text="Generate Shotchart", command=getChart,
                     bg="white", fg="black")
display.create_window(125, 225, window=generate)

t.mainloop()
