import tkinter as tk
from tkinter import ttk

class table():
    def __init__(self, master, headings):
        self.tree = ttk.Treeview(master, columns=headings, show="headings")
        
        for heading in headings:
            self.tree.heading(heading, text=heading, anchor="center") #sets heading text

    def create_heading(self, heading, text):
        self.tree.heading(heading, text=text, anchor="center")

    def define_column(self, heading,width):
        self.tree.column(heading, anchor='center', stretch='no', width=width)

    def insert(self, values):
        self.tree.insert("", tk.END, values=values)

    def pack(self, **kwargs):
        self.tree.pack(**kwargs)