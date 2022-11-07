from tkinter import *
from tkinter import messagebox
import time
from pack.pages.save import save_data
from pack.pages.counter import count
from pack.pages.random_number import generate_number
from pack.pages.random_number import string_number

def check_number(one, two, three, four, gen, root, start, Id,page):
	start_list = list()
	stop_list = list()
	if len(one.get()) == 1 and len(two.get()) == 1 and len(three.get()) == 1 and len(four.get()) == 1:
		c = count()
		for j in start.split(":"):
			start_list.append(int(j))
		answer = [one.get(), two.get(), three.get(), four.get()]
		if answer[0] == gen[0]:
			Entry(root, textvariable=one, state=DISABLED, width=5,justify=CENTER).grid(row=0, column=0, padx=5, ipady=10)

		if answer[1] == gen[1]:
			Entry(root, textvariable=two, state=DISABLED, width=5,justify=CENTER).grid(row=0, column=1, padx=5, ipady=10)

		if answer[2] == gen[2]:
			Entry(root, textvariable=three, state=DISABLED, width=5,justify=CENTER).grid(row=0, column=2, padx=5, ipady=10)

		if answer[3] == gen[3]:
			Entry(root, textvariable=four, state=DISABLED, width=5,justify=CENTER).grid(row=0, column=3, padx=5, ipady=10)

		if answer[::] == gen[::]:
			stop = time.strftime(" %H:%M:%S ", time.gmtime())
			for i in stop.split(":"):
				stop_list.append(int(i))
			hour = abs(stop_list[0] - start_list[0])
			minute = abs(stop_list[1] - start_list[1])
			sec = abs(stop_list[2] - start_list[2])
			timer = f'{hour}:{minute}:{sec}'
			messagebox.showinfo("info",
								f" Username : {Id} ,Number :  {string_number(gen)} ,Time :  {timer}, Count : {len(c)}")
			save_data(Id, level="level 4", time=timer, generate_number=string_number(gen), count=len(c))
			root.destroy()
			page(Id)
	else:
		messagebox.showerror("Error", 'The number entered must be a single digit')

def level_four(Id,page):
	level_Four = Tk()
	level_Four.title('Level Four')
	one_num = StringVar()
	two_num = StringVar()
	three_num = StringVar()
	four_num = StringVar()

	Entry(level_Four, textvariable=one_num, width=5,justify=CENTER).grid(row=0, column=0, pady=5, padx=5, ipady=10)
	Entry(level_Four, textvariable=two_num, width=5,justify=CENTER).grid(row=0, column=1, padx=5, ipady=10)
	Entry(level_Four, textvariable=three_num, width=5,justify=CENTER).grid(row=0, column=2, padx=5, ipady=10)
	Entry(level_Four, textvariable=four_num, width=5,justify=CENTER).grid(row=0, column=3, padx=5, ipady=10)
	start = time.strftime(" %H:%M:%S ", time.gmtime())
	gen = generate_number(4)
	Button(level_Four,width=10, text='Check', command=lambda: check_number(one_num, two_num, three_num, four_num,gen, level_Four, start, Id,page)).grid(row=1,column=1,columnspan=2,pady=5)
	level_Four.mainloop()

