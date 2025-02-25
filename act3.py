#Image makes it better
#NOTE- Use it on terminal- pip install Pillow

from tkinter import *

from PIL import Image, ImageTk
window = Tk()
window.title('Adding image')
window.geometry('400x400')
lab_img= Image.open("image.jpeg")
img1 = ImageTk.PhotoImage(lab_img)

label = Label(window, image=img1, height=200, width=300)


label.pack()

window.mainloop()