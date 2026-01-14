from validation import *
from window import *
from storing_scores import *
import random, time, datetime

def loop(): #Basically the main game
    selction_frame.grid_forget() #Hides rounds selection menu
    selection_but_frame.grid(row=2,column=2,sticky='e') #Places players side
    selection_frame_comp.grid(row=2,column=0,sticky='e') #Places computers side

    rounds = int(rounds_entry.get()) # sets no. rounds to imputted value
    p,c = 0,0 #sets current score to 0

    while rounds > 0:
        choice_entry.set("") # Reset choice entry, preventing from contenuing till a new choice is made
        round_winner = play_round()
        
        p,c = update_tally(p,c,round_winner)
        display_score(p,c)

        tk.Label(game_tab,text="Press any button to continue to next round").grid(row=2,column=1,sticky='s')
        key_press()

        clear_all_window(False)

        rounds -= 1

    clear_all_window(True)
    display_score(p,c)
    store_score(get_date(),p,c) #Pass scores to be stored

    new_score = [str(get_date()),str(p),str(c),overall_winner(p,c)] #A solution as passing directly into display_scores_table caused issues
    display_scores_table([new_score])

    #Game over message
    tk.Label(game_tab, text="Game Over!", font=("Arial", 20)).grid(row=0,column=0)
    tk.Label(game_tab, text="Well done :)", font=("Arial", 20)).grid(row=1,column=0)
    tk.Label(game_tab, text="Press the hand to play again!", font=("Arial", 15)).grid(row=2,column=1)
    rock_img_butt = tk.Button(game_tab, command=num_rounds, image=rock_img1)
    rock_img_butt.grid(row=1,column=1)


def num_rounds(): #Gets the number of rounds to play from the user
    destroy_widgets.remove_all(game_tab,accept=[selection_but_frame,selection_frame_comp,selction_frame])
    num_rounds_display()

    ttk.Button(selction_frame, text="OK", command=loop).grid(row=2,column=2,sticky='w')
    win.update()

def choices():
    return ['rock', 'paper', 'scissors']

def choice_selection(rock_img,paper_img,sicssor_img): #Player and computers choice is made
    computer = random.choice(choices()) #Randomly picks computers choice
    show_images_selction(rock_img,paper_img,sicssor_img) #idk what this done rn

    tk.Button(selection_but_frame, text="Rock",command=lambda:choice_entry.set("rock"),font=("Arial",13),fg='blue').grid(row=2,column=0,sticky='n',pady=5,padx=5)
    tk.Button(selection_but_frame, text="Paper",command=lambda:choice_entry.set("paper"),font=("Arial",13),fg='blue').grid(row=2,column=1,sticky='n',pady=5)
    tk.Button(selection_but_frame, text="Scissors",command=lambda:choice_entry.set("scissors"),font=("Arial",13),fg='blue').grid(row=2,column=2,sticky='n',pady=5,padx=5)

    wait(rock_img,paper_img,sicssor_img)
    print("Computer:", computer," Player:", choice_entry.get())

    return computer, choice_entry.get()


def play_round():
    winner = "" #Sets winner to no one
    computer, player = choice_selection(new_rock_img,new_paper_img,new_scissors_img) #Gets the player and computers choice

    display_animation(new_rock_img,new_paper_img,new_scissors_img,player,computer)

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
        
     
    if winner != 'Tie': tk.Label(game_tab, text=f"{winner} is the winner!",font=("Arial", 15)).grid(row=1,column=1,sticky='n')
    else: tk.Label(game_tab, text="Its a tie!",font=("Arial", 15)).grid(row=1,column=1,sticky='n')
    
    return winner

