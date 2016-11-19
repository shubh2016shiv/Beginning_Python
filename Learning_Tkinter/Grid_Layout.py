'''
Created on Nov 14, 2016

@author: ABC
'''
from tkinter import *
#Define the function
def printSignIn(event):
    print("Sign in Pressed!")

# Define the root, main window to work with
root = Tk();
#defining the widgets
name_Label = Label(root,text="Name")
password_Label = Label(root,text="Password")
name_Entry = Entry(root)
password_Entry = Entry(root)
log_check = Checkbutton(root,text="Keep me logged in")
sign_in_button = Button(root,text="Sign in")
sign_up_button = Button(root,text="Sign up")
cancel_button = Button(root,text="Cancel",command=root.destroy)
# providing Layout
name_Label.grid(row=0,column=0,sticky=E) # E for East , W for West , N for North and S for south.... for aligning purpose
password_Label.grid(row=1,column=0)
name_Entry.grid(row=0,column=1)
password_Entry.grid(row=1,column=1)
log_check.grid(columnspan=2)   # columns span for spanning 2 columns of a row and merging them
sign_in_button.grid(row=3,column=0)
sign_up_button.grid(row=3,column=1)
cancel_button.grid(columnspan=2)
#binding the function to widget
sign_in_button.bind('<Button-1>',printSignIn)
#cancel_button.bind('<Button-1>',root.destroy())
root.mainloop()