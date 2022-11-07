import sqlite3
from tkinter import *
from tkinter import ttk


def show_record(my_tree):
    conn = sqlite3.connect("./database.sqlite")
    cur = conn.cursor()
    query = ("SELECT * FROM score")
    cur.execute(query)
    records = cur.fetchall()
    count_data = 0
    for record in records:
        if count_data % 2 == 0:
            my_tree.insert(parent="", index='end', iid=count_data, text='',
                                    values=(record[1], record[2], record[3], record[4], record[5]), tags=('odd',))
        else:
            my_tree.insert(parent="", index='end', iid=count_data, text='',
                                    values=(record[1], record[2], record[3], record[4], record[5]), tags=('even',))
        count_data += 1
    conn.commit()
    conn.close()



def history_tabel():
    history = Tk()
    history.title('History')
    history.resizable(False, False)
    style = ttk.Style()
    style.theme_use()
    style.configure(history,
                             background="#D3D3D3",
                             foreground='black',
                             rowhieght=25,
                             fieldbackground="#D3D3D3")
    style.map(history, background=[('selected', "black")])
    tree_frame = Frame(history)
    tree_frame.columnconfigure(0, weight=1)
    tree_frame.grid(row=0, column=0)
    my_tree = ttk.Treeview(tree_frame, selectmode='extended')
    my_tree.grid()
    my_tree['column'] = ('Username',
                                  'Count',
                                  'Level',
                                  'Time',
                                  'Generate Number')
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Username", anchor=CENTER, width=140)
    my_tree.column("Count", anchor=CENTER, width=140)
    my_tree.column("Level", anchor=CENTER, width=140)
    my_tree.column("Time", anchor=CENTER, width=140)
    my_tree.column("Generate Number", anchor=CENTER, width=140)
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("Username", text="Username", anchor=CENTER)
    my_tree.heading("Count", text="Count", anchor=CENTER)
    my_tree.heading("Level", text="Level", anchor=CENTER)
    my_tree.heading("Time", text="Time", anchor=CENTER)
    my_tree.heading("Generate Number", text="Generate Number", anchor=CENTER)
    my_tree.tag_configure('odd', font=('', 11), background="lightgreen")
    my_tree.tag_configure('even', font=('', 11), background="white")
    show_record(my_tree)


