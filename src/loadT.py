import pyodbc
import pandas as pd
import tkinter as tk
import re
win=tk.Tk()
conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ellio_6\Documents\etasks-main\src\tasksdb.accdb')
cursor=conn.cursor()
print('Getting Data...')
cursor.execute("select title from TaskDB")
text=cursor.fetchone()
text=str(text)
print(text)
title=eval(text)
title=tk.Label(text=title).pack()
