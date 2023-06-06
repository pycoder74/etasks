import tkinter as tk 
from tkinter import ttk
from tkinter import*
from time import strftime
from datetime import date
from tkinter import messagebox
import TaskCls as ct
from TaskCls import task
import shelve
import python_weather
import asyncio
import os
import quickbar as qb
from task_obj import nTask
import task_obj as nt
from group_obj import group
import group_obj as go
import pickle
import pyodbc
import pandas as pd
import sys
import venv
import loadT
from loadT import load_t
from LoadG import loadG
todohome=tk.Tk()
todohome.state('zoomed')
todohome.title('eTasks')
#places quickbar widget in. see module for geometry managers. 
QB=qb.QuickBar()
#creates frame and places 'add task' and 'add group' button in it.
taskbtnfrme=tk.Frame(todohome, relief='groove', highlightbackground='black', highlightthickness=1, width=500)
taskbtnfrme.pack(anchor='n', side=tk.TOP, fill=X)
#add task button
ctskbtn = tk.Button(taskbtnfrme, width=10, text='+ Add Task')
#add group button
cgroupbtn=tk.Button(taskbtnfrme, width=10, text='+ Add Group')
ctskbtn.pack(padx=3, side="top")
cgroupbtn.pack(padx=3, side="top")

maintskfrme=tk.LabelFrame(todohome, text='All Tasks', labelanchor='n', font=('Calibri 15'), relief='groove', highlightbackground='black', highlightthickness=1, width=250)
maintskfrme.pack_propagate(False)
maintskfrme.pack(anchor='nw', side=tk.LEFT, fill=BOTH, padx=10, pady=5, expand=True)

maingrpfrme=tk.LabelFrame(todohome, text='Groups', labelanchor='n', font=('Calibri 15'), relief='groove', highlightbackground='black', highlightthickness=1, width=250)
maingrpfrme.pack_propagate(False)
maingrpfrme.pack(anchor='nw', side=tk.LEFT, fill=BOTH, padx=10, pady=5, expand=True)

loadT.load_t(maintskfrme)
 
            
def newtaskwin():
    #window is shown when create task button is pressed.
    newtaskwin=Toplevel(todohome)
    newtaskwin.geometry()
    #task name box
    TaskNameLbl=tk.Label(newtaskwin, text='Task Name:').grid(row=1, column=0, pady=5)
    TaskNameEntry=ttk.Entry(newtaskwin, width=100)
    TaskNameEntry.grid(row=1, column=1, pady=5)
    #Group to put the task into
    GroupNameLbl=tk.Label(newtaskwin, text='Group:').grid(row=2, column=0, pady=5)
    GroupNameEntry=ttk.Entry(newtaskwin, width=100)
    GroupNameEntry.grid(row=2, column=1, pady=5)
    #importance of task
    PriorityLbl=tk.Label(newtaskwin, text='Priority:').grid(row=3, column=0, pady=5)
    PriorityEntry=ttk.Combobox(newtaskwin, state="readonly", values=['High', 'Medium', 'Low'], width=97)
    PriorityEntry.grid(row=3, column=1, pady=5)
    #date the task will start
    start_date_lbl=tk.Label(newtaskwin, text='Start Date:').grid(row=4, column=0, pady=5)
    start_date_entry=ttk.Entry(newtaskwin, width=100)
    start_date_entry.grid(row=4, column=1, pady=5)
    #date the task will end
    end_date_lbl=tk.Label(newtaskwin, text='End Date:').grid(row=5, column=0, pady=5)
    end_date_entry=ttk.Entry(newtaskwin, width=100)
    end_date_entry.grid(row=5, column=1, pady=5)
    #time you will start the task
    start_time_lbl=tk.Label(newtaskwin, text='Start Time:').grid(row=6, column=0, pady=5)
    start_time_entry=ttk.Entry(newtaskwin, width=100)
    start_time_entry.grid(row=6, column=1, pady=5)
    #time you will finish the task
    end_time_lbl=tk.Label(newtaskwin, text='End Time:').grid(row=7, column=0, pady=5)
    end_time_entry=ttk.Entry(newtaskwin, width=100)
    end_time_entry.grid(row=7, column=1, pady=5)

    def create_task():
        tName = TaskNameEntry.get()
        gName=GroupNameEntry.get()
        pName=PriorityEntry.get()
        sDate=start_date_entry.get()
        eDate=end_date_entry.get()
        sTime=start_time_entry.get()
        eTime=end_time_entry.get()
        conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/19E.Kelly/Downloads/etasks-main/src/tasksdb.accdb')
        cursor=conn.cursor()
        sql="insert into TaskDB values ('{taskName}', '{priorityName}', '{groupName}', '{startDate}', '{endDate}', '{startTime}', '{endTime}')".format(
            taskName=tName, priorityName=pName, groupName = gName, startDate = sDate, endDate = eDate, startTime = sTime, endTime = eTime)
        try:
            cursor.execute(sql)
            cursor.commit()
            new_tsk=nt.nTask(tName, sDate, eDate, maintskfrme)
            new_tsk.pack(side=tk.TOP, padx=10)
            try:
                notasklbl.destroy()
            except NameError:
                pass
            messagebox.showinfo('eTasks', 'Task saved')
        except pyodbc.IntegrityError as err:
            print(err)
#button to save the task to the db
    create_task_btn=tk.Button(newtaskwin, command=create_task, width=10, text='Save')
    create_task_btn.grid(row=9, column=0)
#adds func newtaskwin to create task button
ctskbtn.configure(command=newtaskwin)
def newgroupwin():
    newgroupwin=Toplevel(todohome)
    groupnamelbl=tk.Label(newgroupwin, text='Group Name')
    groupnamelbl.grid(row=1, column=0)
    groupname_ent=ttk.Entry(newgroupwin, width=100)
    groupname_ent.grid(row=1, column=1)

    def add_group():
        conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/19E.Kelly/Downloads/etasks-main/src/tasksdb.accdb')
        cursor=conn.cursor()
        cursor.execute('select count(*) from TaskDB')
        tasks_num=cursor.fetchall()
        num_str=str(tasks_num)
        tasks_num=''.join(i for i in num_str if i not in "[]()'',")
        num_int=int(tasks_num)
        if num_int == 0:
            tk.messagebox.showwarning(title='eTasks', message='Please add a task first')
            sys.exit()
        groupname=groupname_ent.get()
        try:
            nogrouplbl.destroy()
        except NameError or AttributeError:
            pass

        ngroup=go.group(groupname, maingrpfrme)
        ngroup.pack()
    save_group_btn=tk.Button(newgroupwin, command=add_group, text='Save')
    save_group_btn.grid(row=9, column=0)
        
cgroupbtn.configure(command=newgroupwin) 
    
loadG(maingrpfrme)    
load_t()


    
