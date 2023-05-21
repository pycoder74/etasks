from tkinter import Tk
from json import load, dump

class eTasks(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("eTasks Home")
        self.configure(bg="white")
        self.attributes('-fullscreen', True)

if __name__ == "__main__":
    window = eTasks()
    window.mainloop()
