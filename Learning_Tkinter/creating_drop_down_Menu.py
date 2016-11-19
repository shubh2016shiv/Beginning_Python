'''
Created on Nov 14, 2016

@author: ABC
'''
from tkinter import *
from tkinter import messagebox as msg
def doNothing():
    print("Some text!")
def exit(master):
    answer = msg.askquestion(title="Exit",message="Do you really want to exit?")
    if(answer == "yes"):
        master.destroy()

root = Tk()
main_menu = Menu(root)
root.config(menu=main_menu)

sub_menu = Menu(main_menu)
main_menu.add_cascade(label="File",menu=sub_menu)
sub_menu.add_command(label="Press doNothing()",command=doNothing)
sub_menu.add_separator()
sub_menu.add_command(label="Exit",command=lambda:exit(root))

'''Putting a picture'''
naruto_image = PhotoImage(file="naruto_png.png")
label = Label(root,image=naruto_image)
label.pack()

root.mainloop()