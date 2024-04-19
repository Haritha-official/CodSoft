# PROGRAM FOR ROCK-PAPER SCISSOR GAME
from tkinter import *
import random
def playgame():
    playerchoice = entrybox.get().lower()  # Get player's choice
    computerchoice = random.choice(["rock", "paper", "scissors"])  # Generate computer's choice

    result = determinewinner(playerchoice, computerchoice)  # Determine the winner
    displayresult(playerchoice, computerchoice, result)  # Display the result

def determinewinner(playerchoice, computerchoice):
    if playerchoice == computerchoice:
        return "It's a tie!"
    elif (playerchoice == "rock" and computerchoice == "scissors") or \
         (playerchoice == "scissors" and computerchoice == "paper") or \
         (playerchoice == "paper" and computerchoice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def displayresult(playerchoice, computerchoice, result):
    result_label.config(text=f"\nYour choice: {playerchoice.capitalize()}  "
                              f"\nComputer's choice: {computerchoice.capitalize()}  "
                              f"\nResult: {result}", font=8)

window = Tk()
window.columnconfigure(0, weight = 5)
#Setting showing size of the window
window.geometry("500x300")
#Giving the title
window.title("Rock-Paper-Scissor")
#Setting the backgroundcolor
window.configure(bg="lightgreen")
# Sowing the choice
fontsi = 12
l1 = Label(window, text = "CHOOSE ROCK, PAPER, OR SCISSORS !",font = ("ariel",fontsi), bg = "lightgreen")
l1.grid(row=1, column=0, padx=10, pady=10)
#Creating entry box
txtvar = StringVar()
entrybox = Entry(window, textvariable=txtvar, width=30)
entrybox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
#Creating button
b1 = Button(window, text="PLAY", bg="pink", font=12, command=playgame)
b1.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
#Result label
result_label = Label(window, text="", bg="lightgreen")
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='ew')


window.mainloop()
