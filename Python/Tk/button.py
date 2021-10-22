from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('600x500')

l = Label(root, text='Hola mundo')
def click():
    l.pack()

btn = Button(root, text="Clickeame", command=click,fg='red', background='black')
btn.pack()

root.mainloop()