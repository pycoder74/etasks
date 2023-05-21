import tkinter as tk 
from tkinter import ttk
from tkinter import*
from time import strftime
from datetime import date
from tkinter import messagebox
import shelve
#import python_weather
#import requests
import os
import asyncio
from PIL import Image, ImageTk
class QuickBar(tk.Frame):
    '''class for Tk widget quickbar'''
    def __init__(master=None): #master is changed to window when called in program.
        #frame to house the information in the quickbar
        infoframe = tk.Frame(relief="groove", highlightbackground="black", highlightthickness=1)
        infoframe.pack(fill=X)
        welcomefrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        welcomefrme.pack(side=tk.LEFT, anchor='n', pady=5, padx=5, fill=X)
        Welcome=Label(welcomefrme, font=('calibri', 20), text="eTasks")
        Welcome.pack(anchor='n', side=tk.LEFT, padx=100)
        appfrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        appfrme.pack(side=tk.LEFT, anchor='n', pady=5, padx=5, fill=X)
        applbl=tk.Label(appfrme, font=('calibri', 20), text='[Apps go here]')
        applbl.pack(anchor='n', side=tk.LEFT, padx=100)
        global clock
        global time
        def time():
            ctime=strftime('%H:%M:%S')
            clock.config(text=ctime)
            clock.after(1000, time)

        clockfrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        clockfrme.pack(anchor='n', side=tk.LEFT, pady=5, padx=5, fill=X)

        clock=Label(clockfrme, font=('calibri', 20),
                  foreground='black')
        clock.pack(anchor='center', side=tk.LEFT, padx=100)
        time()

        homefrme=tk.Frame(infoframe, relief="groove", highlightbackground="black", highlightthickness=1)
        homefrme.pack(side=tk.LEFT, anchor='n', pady=5, padx=5, fill=X)
        image=Image.open('Home_Icon.png')
        image=image.resize((50, 44))
        click_btn=ImageTk.PhotoImage(image)

        button=Button(homefrme, image=click_btn, command=None, borderwidth=0)
        button.pack(anchor='w', side=tk.LEFT)

        text=Label(homefrme, text="")
        text.pack()
        mainloop()
if __name__ == '__main__':
    QuickBar()
   
