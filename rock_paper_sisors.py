from validation import *
from window import *
from storing_scores import *
import random, time, datetime

def get_date():
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%x") #Format date to MM/DD/YYYY
    return date_now

def loop():
    #clear_window()
    selction_frame.grid_forget()
    #for widget in selction_frame.winfo_children(): widget.destroy()
    selection_but_frame.grid(row=2,column=2,sticky='e')
    selection_frame_comp.grid(row=2,column=0,sticky='e')
    rounds = int(rounds_entry.get())
    p,c = 0,0

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


def num_rounds():
    clear_window()
    num_rounds_display()

    ttk.Button(selction_frame, text="OK", command=loop).grid(row=2,column=2,sticky='w')
    win.update()

def choices():
    return ['rock', 'paper', 'scissors']

def choice_selection(rock_img,paper_img,sicssor_img):
    computer = random.choice(choices())

    def rock():
        choice_entry.set("rock")
    def paper():
        choice_entry.set("paper")
    def scissors():
        choice_entry.set("scissors")

    show_images_selction(rock_img,paper_img,sicssor_img)

    tk.Button(selection_but_frame, text="Rock",command=rock,font=("Arial",13),fg='blue').grid(row=2,column=0,sticky='n',pady=5,padx=5)
    tk.Button(selection_but_frame, text="Paper",command=paper,font=("Arial",13),fg='blue').grid(row=2,column=1,sticky='n',pady=5)
    tk.Button(selection_but_frame, text="Scissors",command=scissors,font=("Arial",13),fg='blue').grid(row=2,column=2,sticky='n',pady=5,padx=5)

    #tk.Label(selection_but_frame).grid(column=1)

    wait(rock_img,paper_img,sicssor_img)
    #clear_window()
    print("Computer:", computer," Player:", choice_entry.get())

    return computer, choice_entry.get()


def play_round(rock_img=rock_img, paper_img=paper_img, scissors_img=scissors_img):
    winner = ""
    #new_rock_img=rock_img.subsample(5)
    #new_paper_img=paper_img.subsample(14)
    #new_scissors_img=scissors_img.subsample(7)

    computer, player = choice_selection(new_rock_img,new_paper_img,new_scissors_img)

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
        
    #tk.Label(game_tab, text=f"Computer: {computer}",font=("Arial", 20)).grid(row=0,column=0,sticky='e')
    #tk.Label(game_tab, text=f"Player: {choice_entry.get()}",font=("Arial", 20)).grid(row=0,column=2,sticky='w')
     
    if winner != 'Tie': tk.Label(game_tab, text=f"{winner} is the winner!",font=("Arial", 15)).grid(row=1,column=1,sticky='n')
    else: tk.Label(game_tab, text="Its a tie!",font=("Arial", 15)).grid(row=1,column=1,sticky='n')
    
    return winner


#Temp calling

#play_round()