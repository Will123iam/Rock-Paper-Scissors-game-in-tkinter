from validation import *
from window import *
from storing_scores import *
import random, time, datetime

def get_date():
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%x") #Format date to MM/DD/YYYY
    return date_now

def loop():
    clear_window()
    rounds = int(rounds_entry.get())
    p,c = 0,0

    while rounds > 0:
        choice_entry.set("") # Reset choice entry, preventing from contenuing till a new choice is made
        round_winner = play_round()
        
        p,c = update_tally(p,c,round_winner)
        display_score(p,c)

        tk.Label(game_tab,text="Press any button to continue to next round").pack()
        key_press()

        rounds -= 1

    clear_window()
    display_score(p,c)
    store_score(get_date(),p,c) #Pass scores to be stored

    new_score = [str(get_date()),str(p),str(c),overall_winner(p,c)] #A solution as passing directly into display_scores_table caused issues
    display_scores_table([new_score])

    #Game over message
    tk.Label(game_tab, text="Game Over!", font=("Arial", 20)).pack()
    tk.Label(game_tab, text="Press the hand to play again!", font=("Arial", 15)).pack()
    rock_img_butt = tk.Button(game_tab, command=num_rounds, image=rock_img)
    rock_img_butt.pack()


def num_rounds():
    clear_window()
    num_rounds_display()

    ttk.Button(game_tab, text="OK", command=loop).pack()
    win.update()

def choices():
    return ['rock', 'paper', 'scissors']

def choice_selection():
    computer = random.choice(choices())

    def rock():
        choice_entry.set("rock")
    def paper():
        choice_entry.set("paper")
    def scissors():
        choice_entry.set("scissors")

    tk.Button(game_tab, text="rock",command=rock).pack()
    tk.Button(game_tab, text="paper",command=paper).pack()
    tk.Button(game_tab, text="scissors",command=scissors).pack()

    wait()
    clear_window()
    print("Computer:", computer," Player:", choice_entry.get())

    return computer, choice_entry.get()


def play_round(rock_img=rock_img, paper_img=paper_img, scissors_img=scissors_img):
    winner = ""

    computer, player = choice_selection()

    display_animation(rock_img,paper_img,scissors_img)

    if player == computer:
        print("It's a tie!")
        winner = "Tie"
    elif player == 'rock' and computer == 'scissors':
        print("You win! Rock crushes scissors.")
    elif player == 'paper' and computer == 'rock':
        print("You win! Paper covers rock.")
    elif player == 'scissors' and computer == 'paper':
        print("You win! Scissors cut paper.")
    else:
        print("You lost! Computer is better.")
        winner = "Computer"

    if winner == "":
        winner = "Player"
        
    tk.Label(game_tab, text=f"Computer: {computer} Player: {choice_entry.get()}",font=("Arial", 20)).pack() 
    tk.Label(game_tab, text=f"{winner} is the winner!",font=("Arial", 15)).pack()
    return winner
