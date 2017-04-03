from tkinter import *
import os

import AidTrackProduct


def Start():
    AidTrackProduct.mainTk(Toplevel())

mGui = Tk()#Gui variable

mGui.geometry('750x550+200+300') #Size of GUI
mGui.title('AidTrack')#Title
mGui.iconbitmap('logo1icon.ico')
mGui.configure(background='white')

"""GUI content below"""
logo = PhotoImage(file = 'logo1.gif')
w1 = Label(mGui, image=logo).pack(side="top")
#Start Button
buttonStart = Button(mGui,text='Start', command=Start)
buttonStart.pack(side = TOP)

"""GUI content above"""

mGui.mainloop()
