import tkinter as tk
class nTask(tk.Frame):
    def __init__(self, taskname, startDate, endDate, master=None, *args, **kvargs):

        super().__init__(*args, **kvargs)

        taskfrme=tk.Frame(master, relief='groove', highlightbackground='black', highlightthickness=1)
        taskfrme.pack_propagate(True)
        taskfrme.pack(pady=3)

        tasknamefrme=tk.Frame(taskfrme, relief='groove', highlightbackground='black', highlightthickness=1, pady=5, padx=5)
        tasknamefrme.pack_propagate(True)
        tasknamefrme.pack(pady=5, padx=5, side=tk.LEFT)

        tasknamelbl=tk.Label(tasknamefrme, text=taskname)
        tasknamelbl.pack(anchor='center')

        tickBoxfrme=tk.Frame(taskfrme, pady=5, padx=5)
        tickBox=tk.Checkbutton(tickBoxfrme)
        tickBoxfrme.pack(side=tk.RIGHT)
        tickBox.pack(anchor='center')
        
        sdate=tk.Frame(taskfrme, relief='groove', highlightbackground='black', highlightthickness=1, width=320, height=40)
        sdate.pack_propagate(False)
        sdate.pack(side=tk.RIGHT, pady=5, padx=5)
        sdatelbl=tk.Label(sdate, text=f'Starts: {startDate}')
        sdatelbl.pack(side=tk.LEFT)
        
        dDate=tk.Frame(taskfrme, relief='groove', highlightbackground='black', highlightthickness=1, width=320, height=40)
        dDate.pack_propagate(False)
        dDate.pack(side=tk.RIGHT, pady=5, padx=5)
        ddatelbl=tk.Label(dDate, text=f'Ends: {endDate}')
        ddatelbl.pack(side=tk.LEFT)
if __name__ == '__main__':
    root = tk.Tk()
    nTask('name', 'sdate', 'edate', master=root).pack()
    root.mainloop()

