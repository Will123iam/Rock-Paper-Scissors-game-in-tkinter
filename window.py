import tkinter as tk
from tkinter import ttk
#from rock_paper_sisors import *
import time

win=tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("500x400")

rock_img=tk.PhotoImage(file="images/rock.png")
paper_img=tk.PhotoImage(file="images/paper.png")
scissors_img=tk.PhotoImage(file="images/scissors.png")

def clear_window():
    for widget in game_tab.winfo_children():
        widget.destroy()

def display_score(player,computer):
    score_label = tk.Label(game_tab, text=f"Player: {player}  Computer: {computer}", font=("Arial", 15))
    score_label.pack()

selection_menu = ttk.Notebook(win)

#Tab 1
game_tab=ttk.Frame(selection_menu)

def welcome():
    welcome_label = tk.Label(game_tab, text="Welcome to Rock Paper Scissors!", font=("Arial", 20))
    info_label = tk.Label(game_tab, text="Click one the hand to start the game!", font=("Arial", 15))
    
    #Packing
    welcome_label.pack()
    info_label.pack()

def update_tally(player, computer,winner):
    if winner == "Computer": computer += 1
    elif winner == "Tie": pass
    else: player += 1

    return player, computer

rounds_entry = tk.IntVar()
choice_entry = tk.StringVar()

def num_rounds_display():
    tk.Label(game_tab, text="Enter number of rounds to play: ", font=("Arial", 15)).pack()
    ttk.Entry(game_tab, textvariable=rounds_entry).pack()
    win.update()

def display_animation(rock_img, paper_img, scissors_img):

    def wait():
        win.update()
        time.sleep(0.5)

    tk.Label(game_tab, text="Rock...").pack()
    tk.Label(game_tab, image=rock_img).pack()

    wait()
    clear_window()
    tk.Label(game_tab,text="Paper...").pack()
    tk.Label(game_tab, image=paper_img).pack()
    wait()
    clear_window()
    tk.Label(game_tab,text="Scissors...").pack()
    tk.Label(game_tab, image=scissors_img).pack()
    wait()
    clear_window()
    tk.Label(text="Shoot!").pack()
    wait()
    clear_window()
    

selection_menu.add(game_tab, text="Game") #Adds tab to notebook


#Tab 2
tally_tab=ttk.Frame(selection_menu)

    #Table (Using TreeView) - stores player and computer scores at the end of a match
def display_scores_table(scores):
    for round in scores:
        list = []
        for item in round:
            list.append(item)
        scores_table.insert("",tk.END,values=(list))


headings_table1=["Date","Player","Computer","Winner"]

scores_table = ttk.Treeview(tally_tab,columns=(headings_table1), show="headings")

for heading in headings_table1:
    scores_table.heading(heading, text=heading, anchor="center") #sets heading text

scores_table.pack(fill="both", expand=True) 
selection_menu.add(tally_tab, text="Tally") #Adds tab to notebook


#Packing
selection_menu.pack()


