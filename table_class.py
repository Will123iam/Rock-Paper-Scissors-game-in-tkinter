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