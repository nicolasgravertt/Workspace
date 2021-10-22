import builtins
from tkinter import * 

root = Tk()
root.title('Hola mundo: Option menu')
root.geometry('500x500')

def enviar():
    l = Label(root,text=value.get())
    l.pack()

listaChanchito = [
    'Chanchito feliz',
    'Chanchito triste',
    'Chanchito emocionado'
]

value = StringVar()
value.set(listaChanchito[0])

drop = OptionMenu(root,value,*listaChanchito)
drop.pack()

btn = Button(root,text='Enviar',command=enviar)
btn.pack()

root.mainloop()