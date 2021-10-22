from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title('Hola Mundo')

def click():
    messagebox.showwarning('Popup','Holamundo')
    messagebox.showinfo('Popup','Holamundo')
    messagebox.showerror('Popup','Holamundo')

def clickask():
    respuesta = messagebox.askquestion('Popup','Hola mundo:')
    if respuesta == 'yes':
        messagebox.showinfo('Respuesta','la respuesta fue ' + respuesta)
    else:
        messagebox.showinfo('Respuesta','la respuesta fue ' + respuesta)

def clickaskokcancel():
    respuesta = messagebox.askokcancel('Hola Mundo','Desea realizar la accion?')
    if respuesta:
        messagebox.showinfo('Hola mundo','La respuesta fue OK')
    else:
        messagebox.showinfo('Hola mundo','La respuesta fue Cancelar')

btn = Button(root,text='Presioname', command=click)
btn.pack()

btn1 = Button(root,text='Presioname', command=clickask)
btn1.pack()

btn2 = Button(root,text='Presioname', command=clickaskokcancel)
btn2.pack()

root.mainloop()