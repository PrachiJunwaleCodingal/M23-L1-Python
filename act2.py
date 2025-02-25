#act2- getting started with widget

from tkinter import *


window = Tk()
window.title('ACT2-Getting Started with Widgets')
window.geometry('400x400')
label1 = Label(text="Welcome to my app!", fg="white", bg="blue", height=1, width=300)
name_label1 = Label(text="Full Name", bg="pink")
name_entry = Entry()

def display():
    name = name_entry.get()
    global msg
    msg = "Hello "+ name +" Nice to meet you."
    text_box.insert(END, msg)

text_box = Text(height=3)
btn = Button(text="Click", command=display, height=1, bg="green", fg='white')
label1.pack()
name_label1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()
