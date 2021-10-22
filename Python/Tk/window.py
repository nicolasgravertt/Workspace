from tkinter import * 

from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.configure(background='#333333')
root.geometry('386x168')
root.title('Calculadora')

#Solucion 1
#def open():
#    img = ImageTk.PhotoImage(Image.open('cascada.jpg'))
#    top = Toplevel()
#    top.title('Hola mundo, nueva ventana')
#    l2 = Label(top,image=img).pack()
#    l = Label(top,text='Soy un texto en una segunda ventana').pack()
#    top.mainloop()

#Solucion 2
#def open():
#    global img
#    img = ImageTk.PhotoImage(Image.open('cascada.jpg'))
#    top = Toplevel()
#    top.title('Hola mundo, nueva ventana')
#    l2 = Label(top,image=img).pack()
#    l = Label(top,text='Soy un texto en una segunda ventana').pack()
#    top.mainloop()


#Solucion 3
def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l2 = Label(top,image=img).pack()
    l = Label(top,text='Soy un texto en una segunda ventana').pack()

img = ImageTk.PhotoImage(Image.open('cascada.jpg'))
btn = Button(root,text='Click',command=lambda:open(img)).pack()

root.mainloop()
