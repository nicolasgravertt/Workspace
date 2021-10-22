from tkinter import *

root = Tk()
root.title('Hola mundo')

frame = LabelFrame(root,text='Login',pady=10,padx=10)
frame.pack(padx=50,pady=50)

l = Label(frame,text='Estoy dentro de un frame')
btn = Button(frame, text='Salir', command=root.quit)

l.pack()
btn.pack()

root.mainloop()