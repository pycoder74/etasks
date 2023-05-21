import tkinter as tk
import pyodbc
from task_obj import nTask
import task_obj as nt
class group(tk.Frame):
    def __init__(self, name, master=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name=tk.Label(master, text=name)
        self.name.pack(padx=20)

        conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ellio_6\Desktop\Coding\etasks-main\src\tasksdb.accdb')
        cursor=conn.cursor()
        with cursor as source_cursor:
            source_cursor.execute('select count(*) from TaskDB')
            tasks_num=cursor.fetchall()
            num_str=str(tasks_num)
            tasks_num=''.join(i for i in num_str if i not in "[]()'',")
            print(f'Number of tasks to load: {tasks_num}')
            num_int=int(tasks_num)
            source_cursor.execute('select * from TaskDB')
            field_names = [i[0] for i in source_cursor.description]
            field_names = ''.join(field_names)
            fetched_data = source_cursor.fetchmany(num_int)
            fetched_d=str(fetched_data)
            fetched_d=''.join(i for i in fetched_d if i not in "[]()'',")
    
            for i in range(0, num_int):
                taskname = fetched_data[i][0]
                print(taskname)
                priority=fetched_data[i][1]
                print(priority)
                group=fetched_data[i][2]
                print(group)
                sDate=fetched_data[i][3]
                print(sDate)
                eDate=fetched_data[i][4]
                print(eDate)
                sTime=fetched_data[i][5]
                print(sTime)
                eTime=fetched_data[i][6]
                print(f'{eTime} \n')
                if fetched_data[i][2]==name:
                    loaded_task=nt.nTask(taskname, sDate, eDate, self.name)
                    loaded_task.pack()
                else:
                    pass
                
if __name__ == '__main__':
    group('groupname')
