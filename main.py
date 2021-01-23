# This script will display a dialogue box that asks the user for a player name.
# When a valid player name, season year, and season type is inputted, the user can see their player data in the form of a shot chart or a table (maybe, I don't know.)

import player_info
import variable
import tkinter as tk
from tkinter import messagebox

# Button functions.


def check_variables():
    # Will check to see if user inputs are valid

    # First checks to see if season type is toggled
    if variable.seasonType == "":
        messagebox.showinfo(
            title="Toggle Error: No Season Type Found", message="You must toggle a season type.",)
    else:
        # If season type is entered, time to start checking the rest of the variables
        variable.playerName = playerEntry.get()
        variable.playerTeam = teamEntry.get()
        variable.seasonYear = seasonyearEntry.get()
        try:
            player_info.find_player(variable.playerName)
        except:
            messagebox.showinfo(
                title="Input Error", message="Enter a valid player full name\n\nExample: LeBron James")
        try:
            player_info.find_team(variable.playerTeam)
        except:
            messagebox.showinfo(
                title="Input Error", message="Enter a valid team abbreviation\n\nExample: LAL")
        try:
            player_info.find_season(variable.seasonYear)
        except:
            messagebox.showinfo(
                title="Input Error", message="Enter a valid season year\n\nExample: 2020-21")
        # If no except statements are run, display all player and team info and get rid of the dialog box
        # This is where the shot chart will be generated
        else:
            player_info.display_info()
            t.destroy()


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
display = tk.Canvas(t, width=250, height=300, bg="black",
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
display.create_window(125, 95, window=playerEntry)

# Team entry
team_label = tk.Label(
    t, text="What team does he play for? \n(Enter as an abbreviation like PHI)", bg="black", fg="white")
team_label.config(font=("bold", 10))
display.create_window(125, 125, window=team_label)
teamEntry = tk.Entry(t)
display.create_window(125, 150, window=teamEntry)

# Season entry
season_label = tk.Label(t, text="Enter season year (Ex. 2020-21):",
                        bg="black", fg="white")
season_label.config(font=("bold", 10))
display.create_window(125, 175, window=season_label)
seasonyearEntry = tk.Entry(t)
display.create_window(125, 200, window=seasonyearEntry)

# Season type toggle buttons
regButton = tk.Button(text="Regular Season", width=12,
                      relief="raised", command=toggleButton)
poButton = tk.Button(text="Playoffs", width=12,
                     relief="raised", command=toggleButton)
display.create_window(80, 245, window=regButton)
display.create_window(170, 245, window=poButton)

# Execute the main function
generate = tk.Button(text="Generate Shotchart", command=check_variables,
                     bg="white", fg="black")
display.create_window(125, 285, window=generate)

t.mainloop()
