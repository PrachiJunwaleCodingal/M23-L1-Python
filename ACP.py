#here is the product
from tkinter import *
from datetime import date
root = Tk()
root.title('multiplication')
root.geometry('400x300')
label1 = Label(text="Multiplication", fg="white", bg="blue", height=1, width=300)
num1_label1 = Label(text="Enter Number 1", bg="pink")
num1_entry = Entry()
num2_label1 = Label(text="Enter Number 2", bg="pink")
num2_entry = Entry()

def multiply():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    mult = num1*num2
    text_box.insert(END,"Multiplication= ")
    text_box.insert(END, mult)

text_box = Text(height=3)
btn = Button(text="Calculate", command=multiply)
label1.pack()
num1_label1.pack()
num1_entry.pack()
num2_label1.pack()
num2_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()