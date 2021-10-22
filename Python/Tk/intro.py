from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('600x500')

l1 = Label(root, text='Hola mundo mi primera etiqueta')
l2 = Label(root, text='Hola mundo mi primera etiqueta')
l3 = Label(root, text='Hola mundo mi primera etiqueta')
#Label(root, text='Hola mundo mi primera etiqueta').pack()
l1.grid(row=0,column=1)
l2.grid(row=0,column=2)
l3.grid(row=0, column=0)

root.mainloop()