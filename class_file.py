import tkinter as tk
from tkinter import ttk

class table():
    def __init__(self, master, headings):
        self.tree = ttk.Treeview(master, columns=headings, show="headings")
        self.tree.bind("<BackSpace>", lambda event: self.delete_row())    

        self.removed_itmes = []    

    def create_heading(self, heading, text):
        self.tree.heading(heading, text=text, anchor="center")

    def define_column(self, heading,width):
        self.tree.column(heading, anchor='center', stretch='no', width=width)

    def insert(self, values):
        self.tree.insert("", tk.END, values=values)

    def delete_row(self):
        for row in self.tree.selection():
            self.tree.delete(row)

    def delete_row(self):
        for row in self.tree.selection():
            self.removed_itmes.append(self.tree.item(row)["values"])
            self.tree.delete(row)
            print(row,self.removed_itmes)

    def removed_itmes(self):
        return self.removed_items

    def pack(self, **kwargs):
        self.tree.pack(**kwargs)

class tk_frames(tk.Frame):
    def __init__(self,window,colums,rows,*args,**kwargs):
        ttk.Frame.__init__(self,window,*args,**kwargs)

        #Set up colums/rows
        for colum in range(colums): self.columnconfigure(colum,weight=1)
        for row in range(rows): self.rowconfigure(row,weight=1)

    def grids(self,row,column,sticky=None):
        self.grid(row=row,column=column,sticky=sticky)

#class lable_15_arial(tk.Label):
#    def __init__(self,window,row,column,**kwargs):
#        tk.Label.__init__(self,window,font=("Arial",15),**kwargs)
        
        #if use_grid:
#        self.grid(row=row,column=column)

class destroy_widgets():
    def __init__(self):
        pass

    def destroy(*args):
        for widget in [*args]:
            widget.destroy()

    def remove_all(frame,accept=None): #Can pass widgets/frames through to ignore, otherwise deletes everthing within passed frame
        for widget in frame.winfo_children():
            delete=True
            for item in accept:
                if item == widget:
                    print("Cant delete!")
                    delete=False
            if delete:
                widget.destroy()
                print("Deleted!")
        
    def hide_all(frame):
        for widget in frame.winfo_children():
            widget.grid_forget()


class load_image(tk.PhotoImage):
    def __init__(self,file):
        tk.PhotoImage.__init__(self,file=file)





