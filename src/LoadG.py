import pyodbc
import group_obj as go
import tkinter as tk
from tkinter import*
def loadG(master=None):
    global nogrouplbl
    conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/19E.Kelly/Downloads/etasks-main/src/tasksdb.accdb')
    cursor=conn.cursor()
    with cursor as source_cursor:
        source_cursor.execute('select count(*) from TaskDB where Location is not Null')
        g_num=cursor.fetchall()
        num_str=str(g_num)
        g_num=''.join(i for i in num_str if i not in "[]()'',")
        print(f'Number of groups to load: {g_num}')
        num_int=int(g_num)
        if num_int == 0:
            print('No groups to load')
        else:
            source_cursor.execute('select * from TaskDB where Location is not Null')
            field_names = [i[0] for i in source_cursor.description]
            field_names = ''.join(field_names)

            fetched_data = source_cursor.fetchmany(num_int)
            fetched_d=str(fetched_data)
            fetched_d=''.join(i for i in fetched_d if i not in "[]()'',")
            print(fetched_d)
            for i in range(0, num_int):
                groupname=fetched_data[i][2]
                print(groupname)
                loaded_group=go.group(groupname, master)
                loaded_group.pack()
if __name__ == '__main__':
    win=tk.Tk()
    loadG(win)

            
    
           
