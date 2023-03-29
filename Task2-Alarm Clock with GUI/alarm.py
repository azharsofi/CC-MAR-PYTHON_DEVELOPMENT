from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

gui= Tk()
gui.title("Alarm Clock")
gui.geometry("675x350")
gui.config(background="grey")



mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('bt.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(gui)
header.place(x=5,y=5)

head =Label(gui,text="ALARM CLOCK",bg="orange",font=('comic sans',20))
head.pack(fill=X)

panel = Frame(gui)
panel.place(x=5,y=70)

alpp = PhotoImage(file='jp.png')

alp = Label(panel,image=alpp)
alp.grid(rowspan=4,column=3)


atime = Label(panel,text="Set Alarm\n(Hr:Min)",font=('comic sans',16),bg="orange")
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('comic sans',20),width=5)
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Message",font=('comic sans',20))
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=30,pady=5)


start = Button(panel,text="Start alarm",fg="white",bg="blue",font=('comic sans',15),command=th)
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)





gui.mainloop()