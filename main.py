from window import *
from rock_paper_sisors import *
#from table_class import *
import tkinter as tk

#Tab 1 functions
def start_game():
    num_rounds()

welcome()

rock_img_butt = tk.Button(game_tab, command=start_game, image=rock_img)
rock_img_butt.pack()

#Tab 2 functions
display_scores_table(load_scores())

win.protocol("WM_DELETE_WINDOW", store_score_close)
win.mainloop()