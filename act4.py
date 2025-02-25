#login app

from tkinter import *
window = Tk()
window.title('Getting Started with Widgets')
window.geometry('400x300')

lbl1 = Label(text = "Full Name", bg="pink", fg='black')
lbl2 = Label(text = "Email Id", bg="pink", fg='black')
lbl3 = Label(text = "Enter Password", bg="pink", fg='black')

name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")

def display():
	name = name_entry.get()
	msg1 = "Hello "+name
	msg2 =  "\nYou have created new account. Congrats!"
	textbox.insert(END, msg1)
	textbox.insert(END, msg2)

textbox = Text(bg="pink", fg="black")
btn = Button(text = "Create Account", command=display)
lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()

window.mainloop()