from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('600x500')

e = Entry(root,width=60)
e.pack()
e.insert(0,"Ingresa texto:")

def click():
    texto = e.get()
    textvariable.set(texto)
    #l = Label(root,text=texto)
    #l.pack()
    e.delete(0,END)
    #l.configure(text=texto)

btn = Button(root,text='click', command=click)
btn.pack()

textvariable = StringVar()

l = Label(root,textvariable=textvariable)
l.pack()

root.mainloop()