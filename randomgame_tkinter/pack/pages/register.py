import sqlite3
from tkinter import messagebox

def registering(firstname, lastname, email, n_username, n_password, rge,root):
    connection = sqlite3.connect("./database.sqlite")
    c = connection.cursor()
    find_user = ('SELECT username FROM user WHERE username = ?')
    c.execute(find_user, [(n_username.get())])
    if c.fetchall():
        messagebox.showerror('Error!', 'Username Taken Try a Diffrent One.')
    else:
        messagebox.showinfo('Success!', 'Account Created!')
        rge.destroy()
        root()


    insert = 'INSERT INTO user(username,password,firstname,lastname,email) VALUES(?,?,?,?,?)'
    val = ((n_username.get()), (n_password.get()), (firstname.get()), (lastname.get()), (email.get()))
    c.execute(insert, val)
    connection.commit()

