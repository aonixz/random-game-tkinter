from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from pack.pages.menu import menu_page

class Main:
    def __init__(self, master):
        # Window
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.widgets()

    def login(self):

        with sqlite3.connect('./database.sqlite') as db:
            c = db.cursor()


        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.master.destroy()
            menu_page(self.username.get())

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):

        with sqlite3.connect('database.sqlite') as db:
            c = db.cursor()
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        insert = 'INSERT INTO user(username,password,firstname,lastname,email) VALUES(?,?,?,?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get()),(self.firstname.get()), (self.lastname.get()),(self.email.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.grid_forget()
        self.head['text'] = 'LOGIN'
        self.logf.grid()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.grid_forget()
        self.head['text'] = 'Create Account'
        self.crf.grid()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.grid()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.grid()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Label(self.crf, text='Firstname: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.firstname, bd=5, font=('', 15)).grid(row=2, column=1)
        Label(self.crf, text='Lastname: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.lastname, bd=5, font=('', 15)).grid(row=3, column=1)
        Label(self.crf, text='Email: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.email, bd=5, font=('', 15)).grid(row=4, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=5,
                                                                                                         column=1)


