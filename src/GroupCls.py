import tkinter as tk
class ButtonEntry(tk.Frame):
    def __init__(self, parent, button, entry):
        self.button=tk.Button(self, text=entry)
        self.entry=tk.Entry(self.button)

        self.button.pack()
        self.entry.pack()

