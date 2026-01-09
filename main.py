from window import *
from rock_paper_sisors import *
import tkinter as tk

#Tab 1 functions
def start_game():
    num_rounds()

welcome()

rock_img_butt = tk.Button(game_tab, command=start_game, image=rock_img)
rock_img_butt.pack()

#Tab 2 functions
def get_scores():
    names=[['9/1/2026','4','3','Player'], #Temp score stroage
           ['9/1/2026','4','3','Player'],
           ['9/1/2026','4','3','Player'],
           ['9/1/2026','4','3','Player'],]

    return names

display_scores_table(load_scores())

win.mainloop()