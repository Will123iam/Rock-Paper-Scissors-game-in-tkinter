import tkinter as tk
from tkinter import ttk
#from rock_paper_sisors import *
from class_file import *
import time

win=tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("500x300")
win.config(bg='turquoise')

#Loading iamges and re-sizing them
rock_img=load_image("images/rock.png")
paper_img=load_image("images/paper.png")
scissors_img=load_image("images/scissors.png")

rock_img1=rock_img.subsample(3)
new_rock_img=rock_img.subsample(5)
new_paper_img=paper_img.subsample(14)
new_scissors_img=scissors_img.subsample(7)

def clear_all_window(frames):
    for widget in game_tab.winfo_children():
        if widget != selection_but_frame and widget != selection_frame_comp and widget != selction_frame:
            widget.destroy()
    
    for widget in selection_but_frame.winfo_children():
        widget.destroy()
    
    for widget in selection_frame_comp.winfo_children():
        widget.destroy()

    for widget in selction_frame.winfo_children():
        widget.destroy()

    if frames == True:
        selection_but_frame.grid_forget()
        selection_frame_comp.grid_forget()
        #selction_frame.grid_forget()
    

def clear_window(): #Stupid
    for widget in game_tab.winfo_children():
        if widget != selection_but_frame and widget != selection_frame_comp and widget != selction_frame:
            widget.destroy()

def display_score(player,computer):
    score_label = tk.Label(game_tab, text=f"Player: {player}  Computer: {computer}", font=("Arial", 15))
    score_label.grid(row=0,column=1)


s=ttk.Style()
s.theme_use('clam')
s.configure('green_style',background='green')
s.configure('Frame1.TFrame', background='sky blue')

selection_menu = ttk.Notebook(win) #Creates the tabs to switch between

#Tab 1
game_tab = tk_frames(selection_menu,3,3) #Main single player game tab

start_frame = tk_frames(game_tab,3,3,relief='flat',style='Frame1.TFrame') #Inner frame start
selction_frame = tk_frames(game_tab,3,3,relief='flat',style='Frame1.TFrame') #Inner frame rounds selection
selection_but_frame = tk_frames(game_tab,3,3,relief='raised') #Inner frame for player side
selection_frame_comp = tk_frames(game_tab,2,3,relief='raised') #Inner fram for computer

start_frame.grid(row=1,column=1)
#selection_but_frame.grid(row=2,column=2,sticky='e')
#selection_frame_comp.grid(row=2,column=0,sticky='e')

def welcome():
    welcome_label = tk.Label(start_frame, text="Welcome to Rock Paper Scissors!", font=("Arial", 20),bg='sky blue')
    info_label = tk.Label(start_frame, text="Click on the hand to start the game!", font=("Arial", 15),bg='sky blue')
    
    #Packing
    welcome_label.grid(row=0,column=1,sticky='n')
    info_label.grid(row=2,column=1,sticky='n')

def update_tally(player, computer,winner):
    if winner == "Computer": computer += 1
    elif winner == "Tie": pass
    else: player += 1

    return player, computer

rounds_entry = tk.IntVar()
choice_entry = tk.StringVar()
rounds_entry.set(1)

def num_rounds_display():
    selction_frame.grid(row=1,column=1)
    tk.Label(selction_frame,text='Rock, Paper, Scissors game',font=("Arial",15),bg='CadetBlue1').grid(row=0,column=1,sticky='n')
    tk.Label(selction_frame, text="Enter number of rounds to play: ", font=("Arial", 15),bg='dark turquoise').grid(row=1,column=1,sticky='s')
    ttk.Entry(selction_frame, textvariable=rounds_entry).grid(row=2,column=1)
    win.update()

class image_button(tk.Label):
    def __init__(self):
        pass

def show_images_selction(rock_img,paper_img,sicssors_img): #displayes the hand images on player and compters side
    #Player
    tk.Label(selection_but_frame,text="Player:",font=("Arial",15),bg="light goldenrod").grid(row=0,column=0,pady=5,padx=5)
    tk.Label(selection_but_frame, image=rock_img,bg="hot pink").grid(row=1,column=0,padx=5)
    tk.Label(selection_but_frame, image=paper_img,bg="hot pink").grid(row=1,column=1,padx=5)
    tk.Label(selection_but_frame, image=sicssors_img,bg="hot pink").grid(row=1,column=2,padx=5)
    #Info
    tk.Label(game_tab,text="Please make",font=("Arial",20),bg='light cyan').grid(row=0,column=1,sticky='e')
    tk.Label(game_tab,text="your choice!",font=("Arial",20),bg='light cyan').grid(row=0,column=2,sticky='w')
    #comp
    tk.Label(selection_frame_comp,text="Computer:",font=("Arial",15),bg="light goldenrod").grid(row=0,column=0,padx=5,pady=5)
    #tk.Label(selection_frame_comp, image=rock_img,bg="coral").grid(row=1,column=0,sticky='w',padx=5,pady=5)
    tk.Label(selection_frame_comp,text="Choice: ??",font=("Arial",15),bg='sky blue').grid(row=2,column=0,sticky='s',padx=5,pady=5)


def display_animation(rock_img, paper_img, scissors_img,player_choice,computer_choice): #Displays the animation and revials results

    def wait():
        win.update()
        time.sleep(0.5)

    clear_all_window(True)
    selection_but_frame.grids(1,2,'w')
    selection_frame_comp.grids(1,0,"e")

    tk.Label(selection_but_frame,text="Player:",font=("Arial",15),bg="light goldenrod").grid(row=0,column=0,pady=5,padx=5)
    tk.Label(selection_frame_comp,text="Computer:",font=("Arial",15),bg="light goldenrod").grid(row=0,column=0,padx=5,pady=5)
    comp_text=tk.Label(selection_frame_comp,text="Choice: ??",font=("Arial",15),bg='sky blue')
    comp_text.grid(row=2,column=0,sticky='s',padx=5,pady=5)
    tk.Label(selection_but_frame,text=f"Choice: {player_choice}",font=("Arial",15),bg='sky blue').grid(row=2,column=0,sticky='s',padx=5,pady=5)

    rock_label=tk.Label(game_tab, text="Rock...",font=("Arial",15))
    rock_image=tk.Label(selection_but_frame, image=rock_img)
    rock_image2=tk.Label(selection_frame_comp, image=rock_img)
    rock_label.grid(row=0,column=1)
    rock_image.grid(row=1,column=0)
    rock_image2.grid(row=1,column=0)

    wait()
    destroy_widgets.destroy(rock_label,rock_image,rock_image2)

    paper_label=tk.Label(game_tab, text="Paper...",font=("Arial",15))
    paper_image=tk.Label(selection_but_frame, image=paper_img)
    paper_image2=tk.Label(selection_frame_comp, image=paper_img)
    paper_label.grid(row=0,column=1)
    paper_image.grid(row=1,column=0)
    paper_image2.grid(row=1,column=0)

    wait()
    destroy_widgets.destroy(paper_image,paper_image2,paper_label)

    sis_label=tk.Label(game_tab, text="Sicssors...",font=("Arial",15))
    sis_image=tk.Label(selection_but_frame, image=scissors_img)
    sis_image2=tk.Label(selection_frame_comp, image=scissors_img)
    sis_label.grid(row=0,column=1)
    sis_image.grid(row=1,column=0)
    sis_image2.grid(row=1,column=0)

    wait()
    destroy_widgets.destroy(sis_label,sis_image,sis_image2)

    shoot_lable=tk.Label(game_tab,text="Shoot!",font=("Arial",17))
    shoot_lable.grid(row=0,column=1)

    if computer_choice == "rock":   comp=tk.Label(selection_frame_comp, image=rock_img)
    elif computer_choice == "paper": comp=tk.Label(selection_frame_comp, image=paper_img)
    else: comp=tk.Label(selection_frame_comp, image=scissors_img)
    comp.grid(row=1,column=0,padx=10,sticky='e')

    if player_choice == 'rock': pl=tk.Label(selection_but_frame, image=rock_img)
    elif player_choice == 'paper': pl=tk.Label(selection_but_frame, image=paper_img)
    else: pl=tk.Label(selection_but_frame, image=scissors_img)
    pl.grid(row=1,column=0,padx=10,sticky='w')

    comp_text.config(text=f"Choice: {computer_choice}")

    wait()
    shoot_lable.destroy()
    #time.sleep(1)
    #clear_window()
    

selection_menu.add(game_tab, text="Game") #Adds tab to notebook


#Tab 2
tally_tab = tk_frames(selection_menu,0,0)

def display_scores_table(scores): #Table (Using TreeView) - stores player and computer scores at the end of a match
    for round in scores:
        list = []
        for item in round:
            list.append(item)
        table1.insert(list)

#Scores_table
headings_table1=["Date","Player","Computer","Winner"]
widths_table1=[50,100,100,100]

table1 = table(tally_tab, headings_table1)

for heading in headings_table1:
    for width in widths_table1:
        table1.create_heading(heading, heading)
        table1.define_column(heading, width)

table1.pack(fill="both", expand=True)
selection_menu.add(tally_tab, text="Tally") #Adds tab to notebook


#Packing
selection_menu.pack()


