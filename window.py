import tkinter as tk
from tkinter import ttk
#from rock_paper_sisors import *
from class_file import *
import time

win=tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("500x300")
win.config(bg='turquoise')

#Sound
pygame.mixer.init()
start_sound=pygame.mixer.Sound("sound_effects/start.mp3")
rumble=pygame.mixer.Sound("sound_effects/rumble.mp3")
power=pygame.mixer.Sound("sound_effects/power.mp3")
disk=pygame.mixer.Sound("sound_effects/disk.mp3")

#Loading iamges and re-sizing them
rock_img=load_image("images/rock.png")
paper_img=load_image("images/paper.png")
scissors_img=load_image("images/scissors.png")

rock_img1=rock_img.subsample(3)
new_rock_img=rock_img.subsample(5)
new_paper_img=paper_img.subsample(14)
new_scissors_img=scissors_img.subsample(7)

def pick_music(choice):
    if choice == 0: pygame.mixer.music.load("music/one.mp3")
    elif choice == 1: pygame.mixer.music.load("music/two.mp3")
    elif choice == 2: pass
    elif choice == 3: pass

def display_score(player,computer):
    score_label = tk.Label(game_tab, text=f"Player: {player}  Computer: {computer}", font=("Arial", 15))
    score_label.grid(row=0,column=1)

def load_settings():
    settings_record = open("settings_record.txt",'r')
    settings=[]
    count=0
    for line in settings_record: 
        if count == 0 or count == 1: 
            settings.append(eval(line[:-1]))
        elif count == 2: settings.append(int(line[:-1]))
        elif count == 3: settings.append(float(line[:-1]))

        count+=1
    return settings

#Styles creation
blue_style=style_create("blue","clam",'sky blue',items={"Frame"})
cream_style=style_create("cream","clam","navajo white",items={"Frame"})
blanched_almond=style_create("blanched_almond","clam","blanched almond",items={"Frame","Radiobutton"},hover_colours=["peach puff","blanched almond"])


selection_menu = ttk.Notebook(win) #Creates the tabs to switch between

#Tab 1
game_tab = tk_frames(selection_menu,3,3,style='blue.TFrame') #Main single player game tab

start_frame = tk_frames(game_tab,3,3,relief='flat',style='blue.TFrame') #Inner frame start
selction_frame = tk_frames(game_tab,3,3,relief='flat',style='blue.TFrame') #Inner frame rounds selection
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

    frames = [selection_but_frame,selection_frame_comp,selction_frame]
    destroy_widgets.remove_all(game_tab,accept=frames)
    for item in frames: destroy_widgets.remove_all(item)

    if effects_set.get():
        rumble.fadeout(500)
        power.play()

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

    if effects_set.get(): 
        power.fadeout(500)
        disk.play()

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

#Tab 3 - Settings tab

#tk varibles
settings=load_settings()
music_set = tk.BooleanVar(value=settings[0])
effects_set = tk.BooleanVar(value=settings[1])
music_style_set = tk.IntVar(value=settings[2])
volume_set = tk.DoubleVar(value=settings[3])

#Frames
settings_tab = tk_frames(selection_menu,1,4,style="blanched_almond.TFrame")

tk.Label(settings_tab,text="Settings",font=("Arils",20,"bold"),bg="blanched almond").grid(column=0,row=0,sticky='n')

    #Music settings frame
music_frame = tk_frames(settings_tab,4,4,relief='raised',style='cream.TFrame')
music_frame.grids(1,0,sticky='n')

def en_dis(click=True):
    if music_set.get() == False: 
        enable=tk.DISABLED
        pygame.mixer.music.pause()
    else: 
        enable=tk.NORMAL
        if click: pygame.mixer.music.play()

    for widget in style_select_frame.winfo_children():
        widget.config(state=enable)

def change_music():
    pick_music(music_style_set.get())
    pygame.mixer.music.play()

def change_volume(value):
    pygame.mixer.music.set_volume((volume_set.get()/100))

tk.Label(music_frame,text="Music Options",font=("Arils",18,"bold"),bg="navajo white").grid(row=0,column=0,sticky='w',padx=10,pady=5)

#Volume controll
volume_frame=tk_frames(music_frame,3,1,relief='raised',style="blanched_almond.TFrame")
volume_frame.grid(row=0,column=2,pady=10)
tk.Label(volume_frame,text="Min",font=("Arils",10),bg="blanched almond").grid(row=0,column=0,sticky='w',padx=10,pady=10)
tk.Label(volume_frame,text="Max",font=("Arils",10),bg="blanched almond").grid(row=0,column=3,sticky='e',padx=10,pady=10)
ttk.Scale(volume_frame,from_=0,to=100,length=100,orient='horizontal',variable=volume_set,command=change_volume).grid(row=0,column=2)

#Sound on/off
sound_controll_frame = tk_frames(music_frame,1,2,relief='raised',style="blanched_almond.TFrame")
sound_controll_frame.grid(row=1,column=0,padx=10,pady=10)
ttk.Checkbutton(sound_controll_frame,text="Enable Music",variable=music_set,style="blanched_almond.TRadiobutton", command=en_dis).grid(row=0,column=0,padx=10,pady=10)
ttk.Checkbutton(sound_controll_frame,text="Sound Effects",variable=effects_set,style="blanched_almond.TRadiobutton").grid(row=1,column=0,padx=10,pady=10)
#Music style select
style_select_frame = tk_frames(music_frame,2,1,relief='raised',style="blanched_almond.TFrame")
style_select_frame.grid(row=1,column=2,padx=10,pady=10)
ttk.Radiobutton(style_select_frame,text="Style One",value=0,variable=music_style_set,style="blanched_almond.TRadiobutton",command=change_music).grid(row=1,column=1,padx=10,pady=10)
ttk.Radiobutton(style_select_frame,text="Style Two",value=1,variable=music_style_set,style="blanched_almond.TRadiobutton",command=change_music).grid(row=2,column=1,padx=10,pady=10)
ttk.Radiobutton(style_select_frame,text="Style Three",value=2,variable=music_style_set,style="blanched_almond.TRadiobutton",command=change_music).grid(row=1,column=2,padx=10,pady=10)
ttk.Radiobutton(style_select_frame,text="Style Four",value=3,variable=music_style_set,style="blanched_almond.TRadiobutton",command=change_music).grid(row=2,column=2,padx=10,pady=10)

en_dis(click=False)
change_volume(None)

selection_menu.add(settings_tab, text="Settings") #Adds tab to notebook

#Packing
selection_menu.pack()


