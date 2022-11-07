from tkinter import *
from pack.pages.history import history_tabel
from pack.pages.level_FOUR import level_four
from pack.pages.level_FIVE import level_five
from pack.pages.level_SIX import level_six
from pack.pages.level_SEVEN import level_seven
from pack.pages.level_EIGHT import level_eight
from pack.pages.level_NINE import level_nine

def menu_page(Id):
    menu = Tk()
    menu.title(f'Menu')
    Button(menu, text="Level 4", command=lambda: Level_four(menu, Id, menu_page)).grid(row=0, column=0, ipadx=30, ipady=30)
    Button(menu, text="Level 5", command=lambda: Level_five(menu, Id, menu_page)).grid(row=0, column=1, ipadx=30, ipady=30)
    Button(menu, text="Level 6", command=lambda: Level_six(menu, Id, menu_page)).grid(row=0, column=2, ipadx=30, ipady=30)

    Button(menu, text="Level 7", command=lambda: Level_seven(menu, Id, menu_page)).grid(row=1, column=0, ipadx=30, ipady=30)
    Button(menu, text="Level 8", command=lambda: Level_eight(menu, Id, menu_page)).grid(row=1, column=1, ipadx=30, ipady=30)
    Button(menu, text="Level 9", command=lambda: Level_nine(menu, Id, menu_page)).grid(row=1, column=2, ipadx=30, ipady=30)

    menubar = Menu(menu)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Option', menu=file)
    file.add_command(label='History', command=history_tabel)
    file.add_separator()
    file.add_command(label='Exit', command=menu.destroy)
    menu.config(menu=menubar)

def Level_four(root, Id, page):
    root.destroy()
    level_four(Id,page)

def Level_five(root, Id, page):
    root.destroy()
    level_five(Id, page)


def Level_six(root, Id, page):
    root.destroy()
    level_six(Id,page)

def Level_seven(root, Id, page):
    root.destroy()
    level_seven(Id, page)

def Level_eight(root, Id,page):
    root.destroy()
    level_eight(Id,page)

def Level_nine(root, Id, page):
    root.destroy()
    level_nine(Id, page)