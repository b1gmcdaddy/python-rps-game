from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissors") 
root.configure(bg="#000080")


#images
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))


#insert images
user_label = Label(root, image = scissor_img , bg="#000080")
comp_label = Label(root, image = scissor_img_comp, bg="#000080")
user_label.grid(row = 2, column = 0)
comp_label.grid(row = 2, column = 4)


#scoring 
playerScore = Label(root, text = 0, font=("Helvetica", 24, "bold"), fg = "white", bg="#000080")
computerScore = Label(root, text =0, font=("Helvetica", 24, "bold"), fg = "white", bg="#000080")
playerScore.grid(row = 2, column = 3)
computerScore.grid(row = 2, column = 1)

#indicator (NAMES)
comp_indicator = Label(root, font=("Helvetica", 18), text = "COMPUTER", fg = "white", bg="#000080").grid(row = 1, column = 3)
user_indicator = Label(root, font=("Helvetica", 18), text = "USER", fg = "white", bg="#000080").grid(row = 1, column = 1)
logo = Label(root, font=("Helvetica", 24, "bold"), text = "ROCK PAPER SCISSORS", fg = "white", bg="#000080").grid(row = 0, column = 2)


#choice update
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image = rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image = paper_img_comp)
    else:
        comp_label.configure(image = scissor_img_comp)

#for user
    if x == "rock":
        user_label.configure(image = rock_img)
    elif x == "paper":
        user_label.configure(image = paper_img)
    else:
        user_label.configure(image = scissor_img)

    checkWin(x, compChoice)


#buttons
rock = Button(root, width = 20, height = 2, font=("Helvetica", 10, "bold"), text = "ROCK", bg = "black", fg = "white", command = lambda:updateChoice("rock")).grid(row = 3, column = 1)
paper = Button(root, width = 20, height = 2, font=("Helvetica", 10, "bold"), text = "PAPER", bg = "black", fg = "white", command = lambda:updateChoice("paper")).grid(row = 3, column = 2)
scissor = Button(root, width = 20, height = 2, font=("Helvetica", 10, "bold"), text = "SCISSOR", bg = "black", fg = "white", command = lambda:updateChoice("scissor")).grid(row = 3, column = 3)

#messages
msg = Label(root, font = ("Helvetica", 14, "italic"), fg = "white", bg="#000080")
msg.grid(row = 5, column = 2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("TIE")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


root.mainloop()
#end of prog