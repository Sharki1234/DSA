from tkinter import *
import random
screen = Tk(className="Rock Paper Scissors")
screen.geometry("500x500")

user_choice = " "
outcome = 0

def rock_press():
    
    user_choice = "rock"
    play(user_choice)
    user = Label(screen,text = "rock")
    user.grid(row = 3,column = 2)


def paper_press():
    
    user_choice = "paper"
    play(user_choice)
    user = Label(screen,text = "paper")
    user.grid(row = 3,column = 2)
    
def scissors_press():
    
    user_choice = "scissors"
    play(user_choice)
    user = Label(screen,text = "scissors")
    user.grid(row = 3,column = 2)
    
def play(user_input):
    cpu_inputs = ["rock","paper","scissors"]
    outcome = " "
    cpu = random.choice(cpu_inputs)
    if cpu == user_input:
       outcome =("It's a Tie")
    
    elif cpu == "paper" and user_input == "rock":
        outcome = ("You Lose")
    elif cpu == "rock" and user_input == "scissors":
        outcome =("You Lose")
    elif cpu == "scissors" and user_input == "paper":
        outcome =("You Lose")
    
    elif cpu == "rock" and user_input == "paper":
        outcome =("You Win")
    elif cpu == "scissors" and user_input == "rock":
        outcome =("You Win")
    elif cpu == "paper" and user_input == "scissors":
        outcome =("You Win")
    o = Label(screen,text = outcome,fg = "green")
    o.grid(column=2,row=4)

title = Label(screen,text = "Rock,Paper,Scissors game")
user = Label(screen,text = "you chose")
rock = Button(screen,background="red",text = "Rock",fg = "white",width = 10,command=rock_press)
paper = Button(screen,background="green",text = "Paper",fg = "white",width = 10,command=paper_press)
scissors = Button(screen,background="blue",text = "Scissors",fg = "white",width = 10,command=scissors_press)

title.grid(row = 1,column = 1,padx=180,columnspan=3)

rock.grid(row=2,column=1,pady = 100)
paper.grid(row = 2,column=2,pady = 100)
scissors.grid(row = 2,column=3,pady = 100)
user.grid(row = 3,column = 1)

print(outcome)
screen.mainloop()

