import pyodbc
import pandas as pd
import tkinter as tk
def insert():
    conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ellio_6\Desktop\etasks-main\src\tasksdb.accdb')
    cursor=conn.cursor()
    sql="insert into TaskDB values ('{tName}', '{pName}', '{gName}', '{sDate}', '{eDate}', '{sTime}', '{eTime}')".format(tName='Task Name', pName='High', gName = 'Group Name', sDate = '14/03/23', eDate = '15/03/23', sTime = '17:48', eTime = '18:48')
    cursor.execute(sql)
    cursor.commit()
    print('data saved')
def get_data():
    conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ellio_6\Desktop\etasks-main\src\tasksdb.accdb')
    cursor=conn.cursor()
    print('Getting Data...')
    data=pd.read_sql(sql="select * from TaskDB", con=conn)
    print(data)
def delete_all():
    conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ellio_6\Desktop\Coding\etasks-main\src\tasksdb.accdb')
    cursor=conn.cursor()
    print('deleting...')
    cursor.execute("DELETE * FROM TaskDB")
    cursor.commit()
    print('database cleared!')
    cursor.commit()

