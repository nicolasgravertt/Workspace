from tkinter import * 

root = Tk()
root.title('Hola mundo: Checkbox')

root.geometry('500x500')

var = StringVar()
var.set('chanchitofeliz')

c = Checkbutton(root,text='Soy un checkbox',variable=var,onvalue='si',offvalue='chanchitofeliz')
c.pack()

def mostrar():
    l = Label(root,text=var.get())
    l.pack()


btn = Button(root,text='Click',command=mostrar)
btn.pack()

root.mainloop()