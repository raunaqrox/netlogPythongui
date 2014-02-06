#!/usr/bin/python
import sys
import Tkinter
from time import localtime, strftime
mGui=Tkinter.Tk()
mGui.geometry('300x100+500+300')
mGui.title('Netlog')
si=Tkinter.StringVar()
def Enter():
	s=si.get()
	t=strftime("%a, %d %b %Y %I:%M:%S", localtime())
	f = open('netlog.txt', 'a')
	f.write("\n"+t+"\t"+s)
	print  "\n"
mylabel=Tkinter.Label(text="Enter Log",fg="purple",bg="yellow").place(x=10,y=10)
#we could use .grid(row=0,column=0,sticky=E) E-east,W-west of the width
#if we remove the geometry then it takes size of grid
mEntry=Tkinter.Entry(mGui,textvariable=si).place(x=83,y=35)
mButton=Tkinter.Button(mGui,text="Log it",command=Enter).place(x=130,y=65)
mGui.mainloop()