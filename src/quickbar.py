import tkinter as tk 
from tkinter import ttk
from tkinter import*
from time import strftime
from datetime import date
from tkinter import messagebox
import shelve
import python_weather
import requests
import os
import asyncio

class QuickBar(tk.Frame):
    '''class for Tk widget quickbar'''
    def __init__(self, master=None):
        #master is changed to window when called in program.
        super().__init__(master)
        
        #frame to house the information in the quickbar
        infoframe = tk.Frame(relief="groove", highlightbackground="black", highlightthickness=1)
        infoframe.pack(fill=X)
        
        welcomefrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        welcomefrme.pack(side=tk.LEFT, anchor='n', pady=5, padx=5, fill=X)
        
        Welcome=Label(welcomefrme, font=('calibri', 20), text="eTasks")
        Welcome.pack(anchor='n', side=tk.LEFT, padx=100)
        
        tempfrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        tempfrme.pack(side=tk.LEFT, anchor='n', pady=5, padx=5, fill=X)
        
        ctemp=tk.Label(tempfrme, font=('calibri', 20))
        ctemp.pack(anchor='n', side=tk.LEFT, padx=100)
        
        today = date.today()
        cdate = today.strftime("%d/%m/%Y")
        
        dateframe=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        datecal=Label(dateframe, font=('calibri', 20), foreground='black', text=cdate)
        datecal.pack(anchor='center', side=tk.LEFT, padx=100)
        dateframe.pack(anchor='n', side=tk.LEFT, pady=5, padx=5, fill=X)
        
        global clock
        global time
        def time():
            ctime=strftime('%H:%M:%S')
            clock.config(text=ctime)
            clock.after(1000, time)

        clockfrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        clockfrme.pack(anchor='n', side=tk.LEFT, pady=5, padx=5, fill=X)

        clock=Label(clockfrme, font=('calibri', 20), foreground='black')
        clock.pack(anchor='center', side=tk.LEFT, padx=100)
        time()
        
        async def get_weather():
            async with python_weather.Client()as client:
                weather = await client.get("UK")
                temp = weather.current.temperature
                temp=temp+2
                degree_sign = u'\N{DEGREE SIGN}'
                temp=(f'{temp}{degree_sign}C')
                ctemp.configure(text=temp)

        async def main():
            # get the weather first
            await get_weather()

        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        # run the main async function
        asyncio.run(main())

if __name__ == '__main__':
    root = tk.Tk()
    QuickBar(master=root)
    root.mainloop()
