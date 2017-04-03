from tkinter import *


def Track():
    item = e1.get()
    print("Track Product", item)

mGui = Tk()#Gui variable

mGui.geometry('750x550+200+300') #Size of GUI
mGui.title('AidTrack')#Title
mGui.iconbitmap('logo1icon.ico')
mGui.configure(background='white')

"""GUI content below"""
Label(mGui, text="Product Number:").pack(side = TOP)
e1 = Entry(mGui)
e1.pack(side = TOP)
buttonTrack = Button(mGui,text='Track Product', command=Track).pack(side = TOP)
"""GUI content above"""

mGui.mainloop()
