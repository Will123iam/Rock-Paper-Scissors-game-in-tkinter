#Validates imputs
from window import *
import time, datetime, pygame

def animate_comp_selection(x,rock_img,paper_img,sicssor_img,label): #Cycles through all 3 images on computers side

    if x==0:
        label.destroy()
        label=tk.Label(selection_frame_comp, image=rock_img,bg="coral")
        label.grid(row=1,column=0,sticky='w',padx=5,pady=5)
    elif x == 1:
        label.destroy()
        label=tk.Label(selection_frame_comp, image=paper_img,bg="coral")
        label.grid(row=1,column=0,sticky='w',padx=5,pady=5)
    else:
        label.destroy()
        label=tk.Label(selection_frame_comp, image=sicssor_img,bg="coral")
        label.grid(row=1,column=0,sticky='w',padx=5,pady=5)



def validate_str(value,options):
    if value in options: return True
    else: return False

def convert_int(value):
    try: return int(value)
    except:
        print("Invaled input!")
        return False
    
def Score(player,computer,rounds):
    if rounds == 0:
        if player > computer: return "Player wins!"
        elif player == computer: return "It's a tie!"
        else: return "Computer wins!"
    print(player,"-",computer)

def wait(rock_img,paper_img,sicssor_img):
    x=1
    label=tk.Label(selection_frame_comp, image=rock_img,bg="coral")
    while choice_entry.get() == "":
        win.update()
        time.sleep(0.1)
        animate_comp_selection(x,rock_img,paper_img,sicssor_img,label)
        x+=1
        if x >2: x=0

def key_press(frams):
    pressed = False

    def set_pressed(): #need a better way of doing this
        nonlocal pressed
        pressed = True

    win.bind("<KeyPress>",lambda event: set_pressed())

    while not pressed:
        win.update()
        time.sleep(0.1)

    destroy_widgets.remove_all(game_tab,accept=frams)

    return pressed

def get_date():
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%x") #Format date to MM/DD/YYYY
    return date_now

def image_button(window,image,bg,text,image_place=None,butt_place=None): #Just oh no
    label=tk.Label(window,image=image,bg=bg)
    button=tk.Button(window,text=text,font=("Arial",13),fg='blue')

    if image_place: label.grid(**image_place)
    if butt_place: button.grid(**butt_place)

