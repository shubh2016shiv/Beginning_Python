'''
Created on Nov 14, 2016

@author: ABC
'''
from tkinter import *
root = Tk()
topFrame = Frame(root)
topFrame.pack(side=TOP,fill=X)   # fill enables to resize the widget as parent window is resized
lowerFrame = Frame(root)
lowerFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text='Click Me!',fg='white',bg='black')
button1.pack(fill=X)
root.mainloop()
