from window import *
from rock_paper_sisors import *
from class_file import *
import tkinter as tk
import pygame

#Tab 1 functions
def start_game():
    num_rounds()

#Music
pick_music(music_style_set.get())
if music_set.get() == True: pygame.mixer.music.play(-1)

welcome()

#Loads start button
rock_img_scaled=rock_img.subsample(2)
rock_img_butt = tk.Button(start_frame, command=start_game, image=rock_img_scaled)
rock_img_butt.grid(row=1,column=1,sticky='n')

#Tab 2 functions
display_scores_table(load_scores())

win.protocol("WM_DELETE_WINDOW", store_score_close) #Runs a command before closing
win.mainloop()