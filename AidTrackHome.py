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
#Start Buttons

buttonStart = Button(mGui,text='Find Item By Id', command=Start, padx=5)
buttonStart.pack(side = TOP)

Label(mGui, text="    ", background='white', font=("Helvetica", 5)).pack(side = TOP)

# buttonStart = Button(mGui,text='All Items', command=Start, padx=5)
# buttonStart.pack(side = TOP)

"""GUI content above"""

mGui.mainloop()
