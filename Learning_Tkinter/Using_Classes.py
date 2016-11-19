'''
Created on Nov 14, 2016

@author: ABC
'''
from tkinter import *
class printWithButton:
    def __init__(self,master):
        self.master = master
        self.mFrame = Frame(master)
        self.mFrame.pack()
        
        self.printButton = Button(self.mFrame,text="Click here to print",command=self.printIt)
        self.printButton.grid(row=0,column=0)
        self.quitButton = Button(self.mFrame,text="Quit",command=self.master.destroy)
        self.quitButton.grid(row=0,column=1)
    def printIt(self):
        print("Hello Shubham!")

root = Tk()
p = printWithButton(root)
root.mainloop()